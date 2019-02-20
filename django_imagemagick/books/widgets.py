from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

class AdminBookThumbnailWidget(AdminFileWidget):
    
    def render(self, name, value, attrs=None):
        output = []
    
        if value != None:
            output.append(u'<img alt="%s" src="%s" />' % (value.url, value.url,))
        else :
            output.append(_(u'Thumbnail will be automatically generated from uploaded document.'))

        # This is commented out b/c maybe you want to be able to override the thumbnail?
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
    
        return mark_safe(u''.join(output))
