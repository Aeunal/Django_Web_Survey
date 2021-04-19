from photo.models import Photos
from photo.models import Counter
import random

i = 1
types = (1,2)
gender = ('Bedroom', 'Livingroom', 'Bathroom', 'Kitchen')
quality = ('kötü', 'orta', 'iyi')
size = 24
def_ans = ([-1]-size)

while True:
    if len(Photos.objects.filter(using_count=10)) >= len(Photos.objects.all())-23:
        break
    new_ct = Counter(id=i, ids=[], ans1=def_ans, ans2=def_ans, ans3=def_ans)
    i = i + 1
    for e in gender:
        for f in quality:
            for c in types:
                photos = Photos.objects.filter(gender=e, quality=f, type=c)
                while True:
                    photo = photos[random.randint(0, len(photos)-1)]
                    if photo.using_count >= 10:
                        continue
                    photo.using_count = photo.using_count + 1
                    photo.save()
                    new_ct.ids.append(photo.id)
                    break
    new_ct.save()