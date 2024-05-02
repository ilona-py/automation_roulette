from base import Base
from base import BasePage
from data import RouletteResources
from data import RouletteLocators


class Roulette(BasePage):
    url = RouletteResources.url

    @property
    def justify_center_txt(self):
        return Base(self.driver, RouletteLocators.justify_center_txt)

    @property
    def justify_center_button(self):
        return Base(self.driver, RouletteLocators.justify_center_button)

    @property
    def justify_center(self):
        return Base(self.driver, RouletteLocators.justify_center)

    @property
    def bets_block(self):
        return Base(self.driver, RouletteLocators.bets_block)

    @property
    def input_bet_amount(self):
        return Base(self.driver, RouletteLocators.input_bet_amount)

    @property
    def input_border_colour(self):
        return Base(self.driver, RouletteLocators.input_border_colour)

    @property
    def previous_rolls(self):
        return Base(self.driver, RouletteLocators.previous_rolls)

    @property
    def roll_history_title(self):
        return Base(self.driver, RouletteLocators.roll_history_title)

    @property
    def last_100(self):
        return Base(self.driver, RouletteLocators.last_100)

    @property
    def three_numers_of_100(self):
        return Base(self.driver, RouletteLocators.three_numers_of_100)

    @property
    def clear_button(self):
        return Base(self.driver, RouletteLocators.clear_button)
