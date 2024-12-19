from django.contrib import admin
from .models import Camera
from django import forms
from django.utils.safestring import mark_safe


class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'

    class Media:
        js = ('https://api-maps.yandex.ru/2.1/?lang=ru_RU', 'js/custom_map.js')


class CameraAdmin(admin.ModelAdmin):
    form = CameraForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['latitude'].widget.attrs['readonly'] = True
        form.base_fields['longitude'].widget.attrs['readonly'] = True
        return form

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['url'].help_text = mark_safe("""
            <div id="map" style="width: 100%; height: 500px;"></div>
            <script type="text/javascript">
                function init() {
                    var myMap = new ymaps.Map("map", {
                        center: [55.76, 37.64],
                        zoom: 10
                    });

                    myMap.events.add('click', function (e) {
                        var coords = e.get('coords');
                        document.getElementById('id_latitude').value = coords[0];
                        document.getElementById('id_longitude').value = coords[1];
                    });
                }
                ymaps.ready(init);
            </script>
        """)
        return super(CameraAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(Camera, CameraAdmin)
