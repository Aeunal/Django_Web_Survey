from photo.models import Counter, Photos
progress = [0]*31
for idx, i in enumerate(Counter.objects.all()):
  progress[i.count] += 1

total = sum([idx*i for idx, i in enumerate(progress)])
total_surveys = len(Counter.objects.all())
percentage = 100 * ((total/30) / total_surveys)
remaining = progress[0]
print(f"Total progress is < %{percentage:.3f} >\nThere are still {remaining}/{total_surveys} surveys remaining to complete...")

exit()