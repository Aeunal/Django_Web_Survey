from photo.models import Photos

import os

path = 'media/'
#abs_path = "C:/Users/furka/Desktop/form/media"
abs_path = os.path.join(os.getcwd(),"media")
i = 1

for clas in os.listdir(abs_path):
  new_abs_path = os.path.join(abs_path, clas)
  questions = os.listdir(new_abs_path)

  for quest in questions:
    images = os.listdir(os.path.join(new_abs_path, quest))
    if quest == 'Q0_C1':
      quality = 'kotu'
      im_type = 1
    elif quest == 'Q0_C2':
      quality = 'kotu'
      im_type = 2
    elif quest == 'Q1_C1':
      quality = 'orta'
      im_type = 1
    elif quest == 'Q1_C2':
      quality = 'orta'
      im_type = 2
    elif quest == 'Q2_C1':
      quality = 'iyi'
      im_type = 1
    elif quest == 'Q2_C2':
      quality = 'iyi'
      im_type = 2

    for img in images:
      img_path = path + clas + '/' + quest + '/' + img
      new_photos = Photos(id=i, img=img_path, gender=clas, quality=quality, type=im_type)
      new_photos.save()
      i = i+1
