from photo.models import Photos

import os

path = 'media/'
#abs_path = "C:/Users/furka/Desktop/form/media"
abs_path = os.path.join(os.getcwd(),"media")
i = 1

for clas in os.listdir(abs_path):
  questions = os.listdir(os.path.join(abs_path, clas))
  new_abs_path = os.path.join(abs_path, clas)
  for quest in os.listdir(new_abs_path):
    images = os.listdir(os.path.join(new_abs_path, quest))
    if quest == 'Q0_C1':
      quality = 'kotu'
      type = 1
    elif quest == 'Q0_C2':
      quality = 'kotu'
      type = 2
    elif quest == 'Q1_C1':
      quality = 'orta'
      type = 1
    elif quest == 'Q1_C2':
      quality = 'orta'
      type = 2
    elif quest == 'Q2_C1':
      quality = 'iyi'
      type = 1
    elif quest == 'Q2_C2':
      quality = 'iyi'
      type = 2
    for img in images:
      img_path = path + clas + '/' + quest + '/' + img
      new_photos = Photos(id=i, img=img_path, gender=clas, quality=quality, type=type)
      new_photos.save()
      i = i+1
