
"""
Generate random artists for the database.

"""

import random
from ..models import Artist 


def add_random_artist(min_length, max_length):
    """Adds an artist with a random name to the database.

    :param min_length: the minimum length, in letters, of the randomly generated artist's name 
    :param max_length: the maximum length, in letters,  of the randomly generated artist's name 

    :raises ValueError: if max_length is less than min_length
    """

    if max_length < min_length:
        raise ValueError('Max length must be more than min length')

    letters = 'qwertyuiopasdghjklzxcvbnm'
    name = ''.join(random.sample(letters, random.randint(min_length, max_length)))
    Artist.objects.create(name=name)