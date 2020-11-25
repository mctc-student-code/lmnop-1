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

    # check that names returned from db are correct on first loaded page
    def test_first_page_correct_entries(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(1, artists, 2)
        self.assertEqual(artists[0].name, paged_list[0].name)
        self.assertEqual(artists[1].name, paged_list[1].name)

    # check that names returned from db are correct on second loaded page
    def test_second_page_correct_entries(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(2, artists, 2)
        self.assertEqual(artists[2].name, paged_list[0].name)

    # check that the desired number of items are displayed per page
    def test_correct_number_of_items_returned_page_one(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(1, artists, 2)
        self.assertEqual(len(paged_list), 2)

    # check that the desired number of items are displayed per page
    def test_correct_number_of_items_returned_page_two(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(2, artists, 2)
        self.assertEqual(len(paged_list), 1)

    # check that goes to last page
    def test_page_number_higher_than_exists(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(4000, artists, 2)
        #TODO compare page number returned to last available page number
