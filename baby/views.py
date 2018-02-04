from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView
from baby.forms import CurrentDayForm, WeightForm
from baby.models import CurrentDay, HistoryNutrition, BabyWeight
from baby.tools import couting_information
from datetime import datetime


class CurrentDayViews(FormView):
    template_name = 'current_day.html'
    form_class = CurrentDayForm
    success_url = '/baby'

    def form_valid(self, form):
        form.save()
        return super(CurrentDayViews, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CurrentDayViews, self).get_context_data(**kwargs)
        table = CurrentDay.objects.all()
        context['table'] = table
        context['info'] = couting_information(table)
        return context


class BabyWeightView(FormView):
    template_name = 'baby_weight.html'
    form_class = WeightForm
    success_url = '/baby/baby_weight'

    def form_valid(self, form):
        form.save()
        return super(BabyWeightView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BabyWeightView, self).get_context_data(**kwargs)
        context['table'] = BabyWeight.objects.all()
        return context


class HistoryView(ListView):
    template_name = 'history.html'
    queryset = HistoryNutrition.objects.all()


@csrf_exempt
def delete(request):
    CurrentDay.objects.get(id=request.POST['id']).delete()
    return HttpResponse('ok')


@csrf_exempt
def save(request):
    all_food_fusion = all_porridge = all_puree = all_overall_volume = toilet = 0
    all = CurrentDay.objects.all()
    for item in all:
        all_food_fusion += item.food_fusion
        all_porridge += item.porridge
        all_puree += item.puree
        all_overall_volume += item.overall_volume
        toilet += 1 if item.toilet == '+' else 0

    last_date = all.last().date

    HistoryNutrition(date=last_date, food_fusion=all_food_fusion, porridge=all_porridge, puree=all_puree,
                     overall_volume=all_overall_volume, toilet=toilet,
                     age_days=(last_date - datetime.date(datetime(2017, 8, 18))).days).save()

    all.delete()

    return redirect('home')
