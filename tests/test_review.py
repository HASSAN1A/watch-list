import unittest
from app.models import Review


class MovieTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Movie class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_review = Review(1234, "A thrilling new Python Series","https://image.tmdb.org/t/p/w500/khsjha27hbs", "nice movie")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))

    def test_save_review(self):
        """
        Set up method that will run before every Test
        """
        self.new_review = Review.all_reviews.append(self)

