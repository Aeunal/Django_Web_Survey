from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Photos, Counter
from .forms import UpdateForm
from django.contrib import messages
import random
from django.urls import reverse
import random


max_survey_image_count = 30

def update(request, id):
    survey = get_object_or_404(Counter, id=id)
    if survey.count == max_survey_image_count:
        context = {'survey': survey}
        return render(request, 'photo/finish.html', context=context)

    photo = get_object_or_404(Photos, id=survey.ids[survey.count])
    form = UpdateForm(request.POST or None, request.FILES or None, instance=photo)

    
    if form.is_valid():
        survey.ans1[survey.count] = photo.answer1
        survey.ans2[survey.count] = photo.answer2
        survey.ans3[survey.count] = photo.answer3
        survey.count = survey.count + 1 

        if survey.count >= 5:
            form.save()
            photo.save()
        survey.save()
        
        return HttpResponseRedirect("/photo/update/{}".format(id))

    context = {'form' : form, 'photo': photo, 'survey': survey}
    return render(request, 'photo/template.html', context=context)

def update_1(request):
    for i in range(0, max_survey_image_count):
        surveys = Counter.objects.filter(count=i)
        if len(surveys) == 0:
            continue
        break
        
    if len(surveys) != 0:
        rand_int = random.randint(0, len(surveys)-1)
        surveys[rand_int].count = 0
        surveys[rand_int].save()
        return HttpResponseRedirect("/photo/update/{}".format(surveys[rand_int].id))
    else:
        return render(request, 'photo/no_survey.html')
    


