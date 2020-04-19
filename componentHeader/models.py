from cms.models.pluginmodel import CMSPlugin

from django.db import models

class ComponentHeader(CMSPlugin):
    ComponentHeader_title = models.CharField(max_length=150, default='YOUR FAVORITE SOURCE OF FREE BOOTSTRAP THEMES')
    ComponentHeader_subtitle = models.CharField(max_length=150, default='Start Bootstrap can help you build better websites using the Bootstrap Framework! Just download a theme and start customising, no strings attached!')
    ComponentHeader_button = models.CharField(max_length=150, default='Find out more')
