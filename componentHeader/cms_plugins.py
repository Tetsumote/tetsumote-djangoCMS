from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import ComponentHeader as ComponentModelHeader

@plugin_pool.register_plugin
class ComponentHeader(CMSPluginBase):
    model = ComponentModelHeader
    module = _("Components")
    name = _("ComponentHeader") 
    render_template = "ComponentHeader.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ComponentHeader, self).render(context, instance, placeholder)
        return context