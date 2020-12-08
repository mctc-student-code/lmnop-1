from django.shortcuts import render, redirect, get_object_or_404
from ..models import Venue, Artist, Note, Show
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.db.models.functions import Lower

from django.test import TestCase
from ..models import Artist, Venue, Show, Note, User
from datetime import datetime
from django.utils import timezone
from django.db.models import Count



class TestTopShows(TestCase):

    def setUp(self):

        # Set up provides sample data for your test
        for i in range(5):
            artist = Artist(name=f'Number{i+1}')
            artist.save()
            venue = Venue(name=f'venue{i+1}', city=f'city{i+1}', state=f'state{i+1}')
            venue.save()
            show = Show(show_date=timezone.now(), artist=Artist(id=i+1), venue=Venue(i+1))
            show.save()
            note = Note(show=Show(f'{i+1}'), user=User(id=1), title=f'title{i+1}', text=f'text{i+1}')
            
            note.save()

        for i in range(4):
            more_note = Note(show=Show(f'{1}'), user=User(id=1), title=f'title{2}', text=f'text{2}')
            more_note.save()

        for i in range(3):
            more_note = Note(show=Show(f'{2}'), user=User(id=1), title=f'title{2}', text=f'text{2}')
            more_note.save()
        for i in range(2):
            more_note = Note(show=Show(f'{3}'), user=User(id=1), title=f'title{2}', text=f'text{2}')
            more_note.save()

        for i in range(1):
            more_note = Note(show=Show(f'{3}'), user=User(id=1), title=f'title{2}', text=f'text{2}')
            more_note.save()


    def test_first_show_5_notes(self):
        pass
        #response = self.client.get(reverse('show_most_notes'))

        ##shows_expected = list(Show.objects.annotate(num_notes=Count('note')).order_by('-num_notes'))
        #shows_provided = list(response.context['show'])
        #self.assertEqual(shows_expected, shows_provided)

    



        #paged_list = helpers.pg_records(1, notes, 2)
        












    #fixtures = [ 'testing_users', 'testing_artists', 'testing_venues', 'testing_shows', 'testing_notes' ]

    #def test_show_with_most_notes(self):
        #most_notes = Show.objects.count()
        #response = self.client.get(reverse('txt/show_most_notes', {'artist': 2, 'venue': 1}))
        #self.assertEqual( Show.objects.count(), most_notes)

        #reviewed_shows = reverse('show_most_notes')
        #self.assertContains(response,reviewed_shows)













    #def test_artist_search_no_search_results(self):
        #response = self.client.get( reverse('show_most_notes') , {'artist' : 'Michael Jackson', 'venue': 'Us Bank Stadium'} )
        #self.assertNotContains(response, 'Michajsjsjs')
        #self.assertNotContains(response, 'HDFSKJFSDJF')
        #self.assertNotContains(response, 'jACKSON')
        # Check the length of artists list is 0
        #self.assertEqual(len(response.context['artists']), 200)


    #def setUp(self):
        # Every test needs access to the request factory.
        #self.factory = RequestFactory()
        #self.show = Show.objects.annotate(artist='Michael Jackson', venue='US Bank Stadium', show_date='Dec. 7, 2020, noon')        
        

    #def test_template_used(self):
        #request = self.factory.get('/template/')
        #response = template(request)
        #print(response.status_code)
        #self.assertEqual(response.status_code, 200)        
        #response = self.client.get('/')
        #self.assertTemplateUsed(response, 'show_most_notes.html')


   

    #def test_correct_template_used_for_most_reviwed_shows(self):
     #   response = self.client.get('show_most_notes')
      #  self.assertTemplateUsed(response, 'lmn/notes/show_most_notes.html/')
     
    #fixtures = [ 'testing_users', 'testing_artists', 'testing_venues', 'testing_shows', 'testing_notes']

    # setUp provides sample data to test data base. Data is created everytime tests are run and test db is destroyed
    # after tests are complete
    #def setUp(self):
        #user = User(username='user', password='password')
        #user.save()
        #for i in range(3):
            #artist = Artist(name=f'Number{i+1}')
            #artist.save()
            ##venue = Venue(name=f'venue{i+1}', city=f'city{i+1}', state=f'state{i+1}')
            #venue.save()
            #notes = Note(title=f'id{i+1}')
            #notes.save()
            # timezone will check the django settings to get the appropriate time for now
            #show = Show(show_date=timezone.now(), artist=Artist(id=i+1), venue=Venue(i+1), notes=Note(title=i+1))
            #show.save()

    #def test_correct_entries_artist(self):
        #artists = Artist.objects.annotate(num_notes=Count('note')).order_by('-num_notes')
        #list = pg_records(1, artists, 2)
        #self.assertEqual(artists[0].note, list[0].note)
        #self.assertEqual(artists[1].note, list[1].note)

    #def test_correct_entries_venues(self):
        #venues = Venue.objects.annotate(num_notes=Count('note')).order_by('-num_notes')
        #list = pg_records(2, venues, 2)
        #self.assertEqual(venues[2].note, list[0].note)
        #self.assertEqual(venues[2].note, list[1].note)

    #def test_most_revied_shows(self):
        #response = self.client.get(reverse('show_most_notes'))
        #self.assertTemplateUsed(response, 'lmn/notes/show_most_notes.html')


    #def test_shows_with_most_noted(self):
       ## response = self.client.get(reverse('show_most_notes'))
       # expected_shows = list(Show.objects.annotate(num_notes=Count('note')).order_by('-num_notes'))
        #context = response.context['shows']
        #context.sort(context)
        #first = context[0]
        #self.assertEqual(first.num_notes, 2)


    #def test_show_with_most_notes(self):
        #most_notes = Show.objects.create(Artist='Michael Jackson', Venue="US Bank Stadium" )
        #response = self.client.get(reverse('artist_list'), {'artist': 'Michael Jackson'}, {'venue': 'US Bank Stadium'})
        
        #self.assertEqual(1,  response)

    #def test_custom_query(self):
    # Put whatever code you need here to insert the test data
        #response = Show.objects.annotate(num_notes=Count('note')).order_by('-num_notes')
        #self.assertEqual(response.annotate('notes'))
        #self.assertEqual({notes.pk for notes in response}, 0)
        #self.assertEqual(
        #[notes.annotated_value for notes in response],note
        
    #)

        