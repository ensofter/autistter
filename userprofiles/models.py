# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


GENDER =(('мужчина','Мужчина'),('женщина','Женщина'),('трап','Трап'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name="profile", verbose_name=_(u'User'))
    phone = models.PositiveIntegerField(null=True, blank=True, verbose_name=_(u"Телефон"))
    gender = models.CharField(max_length=40, blank=True, verbose_name=_(u'Пол'), choices=GENDER)
    avatar = models.ImageField(upload_to='userprofiles/avatars', null=True, blank=True, verbose_name=_(u"Аватар"))
    completion_level = models.PositiveSmallIntegerField(default=0, verbose_name=_(u'Процент заполнения профиля'))
    email_is_verified = models.BooleanField(default=False, verbose_name=_(u'Email верифицирован'))
    personal_info_is_completed = models.BooleanField(default=False, verbose_name=_(u'Персональная информация заполнена'))

    class Meta:
        verbose_name=_(u'User profile')
        verbose_name_plural = _(u'User profiles')
        
    def __unicode__(self):
        return u"User profile: %s" % self.user.username
    
    def get_completion_level(self):
        completion_level = 0
        if self.email_is_verified:
            completion_level += 50
        if self.personal_info_is_completed:
            completion_level += 50
        return completion_level
        
    def update_completion_level(self):
        self.completion_level = self.get_completion_level()
        self.save()
        return

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])