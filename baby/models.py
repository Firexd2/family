from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
import re


def validator_time(value):
    if not re.match('\d\d:\d\d', value):
        raise ValidationError(u'Время необходимо ввести в формате 00:00')


class CurrentDay(models.Model):
    time = models.CharField('Время', max_length=5, validators=[validator_time])
    food_fusion = models.IntegerField('Смесь', null=True, blank=True)
    porridge = models.IntegerField('Каша', null=True, blank=True)
    puree = models.IntegerField('Пюре', null=True, blank=True)
    overall_volume = models.IntegerField('Общий объем', null=True, blank=True)
    toilet = models.CharField('Туалет', max_length=10, null=True, blank=True)
    date = models.DateField('Дата', default=datetime.now, blank=True)

    def __str__(self):
        return '%s' % self.time

    def save(self, *args, **kwargs):
        if not self.food_fusion:
            self.food_fusion = 0
        if not self.porridge:
            self.porridge = 0
        if not self.puree:
            self.puree = 0

        if eval(self.toilet):
            self.toilet = '+'
        else:
            self.toilet = '-'

        self.overall_volume = self.food_fusion + self.porridge + self.puree

        super(CurrentDay, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Питание текущего дня'
        verbose_name_plural = 'Список приема пищи за сегодня'


class HistoryNutrition(models.Model):
    date = models.DateField('Дата')
    age_days = models.IntegerField('Возраст')
    food_fusion = models.IntegerField('Смесь')
    porridge = models.IntegerField('Каша')
    puree = models.IntegerField('Пюре')
    overall_volume = models.IntegerField('Общий объем')
    toilet = models.IntegerField('Туалет')

    def __str__(self):
        return '%s' % self.age_days

    class Meta:
        verbose_name = 'История питания'
        verbose_name_plural = 'История питания'


class BabyWeight(models.Model):
    week = models.IntegerField()
    weight = models.IntegerField()
    lenght = models.IntegerField()

    def __str__(self):
        return '%s, %s, %s' % (self.week, self.lenght, self.weight)

    class Meta:
        verbose_name = 'Развитие малыша'
        verbose_name_plural = 'Развитие малыша'
