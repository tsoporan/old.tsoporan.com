from django import forms
from django.conf import settings
from django.contrib.sites.models import Site

req = {'class': 'required'}

class ContactForm(forms.Form):
    def __init__(self, meta=None, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.meta = meta
    
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=req), label="Name", error_messages={'required': "Your name please."})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(req, max_length=200)), label="Your email", error_messages={'required': "Need an email, to be able to get back in touch!"})
    message = forms.CharField(widget=forms.Textarea(attrs=req), label="Message", error_messages={'required': "You've left no message =("})
    
#Grabbed from ubernostrum's django-contact-form - https://bitbucket.org/ubernostrum/django-contact-form
class AkismetContactForm(ContactForm):
    def clean_message(self):
        """
        Perform Akismet validation of the message.
        
        """
        if 'message' in self.cleaned_data and getattr(settings, 'AKISMET_API_KEY', ''):
            from akismet import Akismet
            from django.utils.encoding import smart_str
            akismet_api = Akismet(key=settings.AKISMET_API_KEY,
                                  blog_url='http://%s/' % Site.objects.get_current().domain)
            if akismet_api.verify_key():
                akismet_data = { 'comment_type': 'comment',
                                 'referer': self.meta.get('HTTP_REFERER', ''),
                                 'user_ip': self.meta.get('REMOTE_ADDR', ''),
                                 'user_agent': self.meta.get('HTTP_USER_AGENT', '') }
                if akismet_api.comment_check(smart_str(self.cleaned_data['message']), data=akismet_data, build_data=True):
                    raise forms.ValidationError(u"Akismet thinks this message is spam")
        return self.cleaned_data['message']
