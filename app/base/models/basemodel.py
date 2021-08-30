

import os
import csv

from django.db import models
from django.db.models import ProtectedError
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class ERPBase(models.Model):
    DateCreation = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    DateModified = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True, blank=True, null=True)
    company_id = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    User = models.CharField(_('User'), max_length=80)  # "TODO"

    class Meta:
        ordering = ['pk']
        abstract = True

    def get_absolute_url(self):
        return reverse('{}:detail'.format(self._meta.object_name), kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)

            message = _("'The %(obj_name)s was deleted successfully.'") % {
                'obj_name': self._meta.verbose_name}
            return "messages.success(request, {})".format(message)
        except ProtectedError:
            message = _("'The %(obj_name)s cannot be deleted, certain information on system depends on this.'") % {
                'obj_name': self._meta.verbose_name}
            return "messages.error(request, {})".format(message)

    @classmethod
    def LoadData(cls, type, company_id):
        ToModel = cls
        toModelName = cls.__name__
        app_name = cls._meta.app_label
        folder_apps = format(settings.BASE_DIR) + \
            '/apps/' + format(app_name) + '/' + type
        route_csv = folder_apps + '/'+toModelName+'.csv'
        if os.path.isfile(route_csv):
            with open(route_csv) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    mydic = row
                    lines = ""
                    cont = 0
                    for key, value in mydic.items():
                        cont += 1
                        lines += key + "=" + "'" + value + "'"
                        if cont < len(mydic):
                            lines += ","
                    lines = "ToModel(" + lines
                    lines = lines + ",company_id='" + str(company_id) + "')"
                    lines.replace('"', '')
                    _Model = eval(lines)
                    _Model.save()
        else:
            print(route_csv)
