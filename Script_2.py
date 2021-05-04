from photo.models import Photos
from photo.models import Counter
import random

i = 1
types = (1,2)
gender = ('Bedroom', 'Livingroom', 'Bathroom', 'Kitchen')
quality = ('kotu', 'orta', 'iyi')

image_count = 30#24
def_ans = [-1]*image_count
max_using_count = 10

total_image_in_db = len(Photos.objects.all())

while True:
    if len(Photos.objects.filter(using_count=max_using_count)) >= (total_image_in_db - image_count - 1):
        break
    
    new_ct = Counter(id=i, ids=[], ans1=def_ans, ans2=def_ans, ans3=def_ans)
    i = i + 1

    for e in gender:
        for f in quality:
            for c in types:

                """
                if e == "Livingroom":

                    photos = Photos.objects.filter(gender=e, quality=f, type=c)
                    photo_to_use = []
                    while True:
                        photo = photos[random.randint(0, len(photos)-1)]

                        if photo.using_count < max_using_count:

                            photo_not_in_use = True
                            for in_use in photo_to_use:
                                if photo.id == in_use.id:
                                    photo_not_in_use = False

                            if photo_not_in_use:
                                photo_to_use.append(photo)
                        
                        if len(photo_to_use) >= 2:
                            break
                        
                    for in_use in photo_to_use:
                        in_use.using_count = in_use.using_count + 1
                        in_use.save()
                        new_ct.ids.append(in_use.id)

                else:
                """
                if e == "Livingroom":
                    photos = Photos.objects.filter(gender=e, quality=f, type=c)
                    while True:
                        photo = photos[random.randint(0, len(photos)-1)]
                        if photo.id not in new_ct.ids:
                            break
                    photo.save()
                    new_ct.ids.append(photo.id)
                

                photos = Photos.objects.filter(gender=e, quality=f, type=c)
                while True:
                    photo = photos[random.randint(0, len(photos)-1)]
                    if photo.using_count < max_using_count:
                        break
                photo.using_count = photo.using_count + 1
                photo.save()
                new_ct.ids.append(photo.id)

    new_ct.save()