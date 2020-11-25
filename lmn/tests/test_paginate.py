from django.test import TestCase
from lmnop_project import helpers
from ..models import Artist, Venue, Show


# test will take a small sample of data using the pg_records function and assertequals
class TestListWithPageData(TestCase):

    def setUp(self):
        for i in range(3):
            artist = Artist(name=f'Number{i+1}')
            artist.save()  # must save the new artist, then get id
            venue = Venue(name=f'venue{i+1}', city=f'city{i+1}', state=f'state{i+1}')
            venue.save()

    def test_first_page_correct_entries(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(1, artists, 2)
        self.assertEqual(artists[0].name, paged_list[0].name)
        self.assertEqual(artists[1].name, paged_list[1].name)

    def test_second_page_correct_entries(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(2, artists, 2)
        self.assertEqual(artists[2].name, paged_list[0].name)

    def test_correct_number_of_items_returned_page_one(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(1, artists, 2)
        self.assertEqual(len(paged_list), 2)

    def test_correct_number_of_items_returned_page_two(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(2, artists, 2)
        self.assertEqual(len(paged_list), 1)