from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Photos, Counter
from .forms import UpdateForm
from django.contrib import messages
import random
from django.urls import reverse

#import logging
#stdlogger = logging.getLogger(__name__)
#dbalogger = logging.getLogger('dba')


types = (1,2)
gender = ('Bedroom', 'Livingroom', 'Bathroom', 'Kitchen')
quality = ('kotu', 'orta', 'iyi')

max_survey_image_count = 30
image_count = 30#24
def_ans = [-1]*image_count
max_using_count = 10


def update(request, id):
    print("Entering debug msg", id, request)
    #stdlogger.debug("Entering update/id method")


    survey = get_object_or_404(Counter, id=id)

    photo = get_object_or_404(Photos, id=survey.ids[survey.count])
    form = UpdateForm(request.POST or None, request.FILES or None, instance=photo)
    print(form.is_valid())
    
    #print(photo.answer1)

    if form.is_valid():
        survey.ans1[survey.count] = photo.answer1
        survey.ans2[survey.count] = photo.answer2
        survey.ans3[survey.count] = photo.answer3
        survey.count = survey.count + 1 

        form.save()
        photo.save()
        survey.save()

        #return HttpResponseRedirect("/photo/update/{}".format(id))

    if survey.count == max_survey_image_count:
        context = {'survey': survey}
        return render(request, 'photo/finish.html', context=context)

    photo = get_object_or_404(Photos, id=survey.ids[survey.count])
    context = {'form' : form, 'photo': photo, 'survey': survey}
    print("Rendered template with:", context)

    return render(request, 'photo/template.html', context=context)

def update_1(request):
    for i in range(0, max_survey_image_count):
        surveys = Counter.objects.filter(count=i)
        if len(surveys) == 0:
            continue
        break
        
    if len(surveys) > 0:
        rand_int = random.randint(0, len(surveys)-1)
        surveys[rand_int].count = 0
        surveys[rand_int].save()
        return HttpResponseRedirect("/photo/update/{}".format(surveys[rand_int].id))

    """
    else:

        all_counters = Counter.objects.all()
        if len(all_counters) <= 0:
            print("Populating DB from scratch.")

            i = 1
            total_image_in_db = len(Photos.objects.all())

            for photo in Photos.objects.all():
                photo.using_count = 0
                photo.save

            while True:
                if len(Photos.objects.filter(using_count=max_using_count)) >= (total_image_in_db - image_count - 1): break
                
                print(f"\r Creating new Counter object {i}", end="")
                new_ct = Counter(id=i, ids=[], ans1=def_ans, ans2=def_ans, ans3=def_ans)
                i = i + 1

                for e in gender:
                    for f in quality:
                        for c in types:
                            if e == "Livingroom":
                                for i in range(2):
                                    photos = Photos.objects.filter(gender=e, quality=f, type=c)
                                    while True:
                                        photo = photos[random.randint(0, len(photos)-1)]
                                        if photo.id not in new_ct.ids and photo.using_count < max_using_count*2:
                                            break
                                    photo.using_count = photo.using_count + 1
                                    photo.save()
                                    new_ct.ids.append(photo.id)
                            else:
                                photos = Photos.objects.filter(gender=e, quality=f, type=c)
                                while True:
                                    photo = photos[random.randint(0, len(photos)-1)]
                                    if photo.id not in new_ct.ids and photo.using_count < max_using_count:
                                        break
                                photo.using_count = photo.using_count + 1
                                photo.save()
                                new_ct.ids.append(photo.id)

                new_ct.save()
                print(f"\r Finished Creating new Counter object {i}", end="")

        print("Finished Script-2")      
        return HttpResponseRedirect("/photo/update_1/")
        """

    return render(request, 'photo/no_survey.html')
    



"""
python manage.py shell -c "from photo.models import Counter; print(len(Counter.objects.all()))"
python manage.py shell -c "from photo.models import Photos; print(len(Photos.objects.all()))"

python manage.py shell -c "from photo.models import Counter; Counter.objects.all().delete()"

python manage.py flush
python manage.py shell -c "import Script_1"
python manage.py shell -c "import Script_2"

python manage.py runserver 

"""