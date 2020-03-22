from django import forms

from .models import Channel

class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        fields = ('channel_name','channel_url','channel_url','video_count','channel_location','subscriber_count','email')