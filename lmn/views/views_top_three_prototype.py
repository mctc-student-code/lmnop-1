from django.db.models import Count
from ..models import Venue, Artist, Note, Show

# Query collects the show_ids and counts how many times the id appears in notes
counter = Note.objects.values('show_id').annotate(note_count=Count('show_id'))

# convert query into a list of objects
counter = list(counter)
counter_dict = {}
top_three_key_list = []

# converts each objects element value into a new dictionary. Contains the show id as the key and the number notes as the value
for i in range(len(counter)):
    key = counter[i]['show_id']
    value = counter[i]['note_count']
    counter_dict[key] = value

# if the number of notes is less than three, only collects the max number for the range of the original list extracts
# the show id with the highest value, adds it to the list and sets the dictionary value to zero to make sure it isnt
# counted twice
if len(counter) > 2:
    for i in range(3):
        max_key = max(counter_dict, key=counter_dict.get)
        top_three_key_list.append(max_key)
        counter_dict[max_key] = 0

else:
    for i in range(len(counter)):
        max_key = max(counter_dict, key=counter_dict.get)
        top_three_key_list.append(max_key)
        counter_dict[max_key] = 0
