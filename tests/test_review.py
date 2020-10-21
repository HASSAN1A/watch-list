import unittest
from app.models import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_review = Review(12345, 'Review for movies', "https://image.tmdb.org/t/p/w500/jdjdjdjn",
                                 'This movie is the best thing since sliced bread')

    def tearDown(self):
        Review.clear_reviews()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))
