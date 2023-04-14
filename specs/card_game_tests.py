import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):
    def setUp(self):
        self.cards = CardGame()
        self.card1 = Card("heart", 1)
        self.card2 = Card("spade", 5)
    

    def test_can_check_fors_ace(self):
        self.assertEqual(True, self.cards.check_for_ace(self.card1))
    
    def test_highest_card(self):
        self.assertEqual(self.card2, self.cards.highest_card(self.card1, self.card2) )

    def test_can_get_list(self):
        self.assertEqual([self.card1, self.card2], self.cards.cards_list(self.card1, self.card2))

    def test_can_get_total(self):
        card_list = self.cards.cards_list(self.card1, self.card2)
        cards_total = self.cards.cards_total(card_list)
        self.assertEqual("You have a total of 6", cards_total )
        