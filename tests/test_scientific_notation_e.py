import allure
from data import RouletteResources


@allure.title("Verify that scientific notation letter 'e' can be entered | Test Case 6")
def test_scientific_notation_e(roulette, open_roulette):
    roulette.input_bet_amount.send_keys('1e')
    roulette.input_bet_amount.click()
    assert roulette.input_border_colour.get_css_value('border-color') == RouletteResources.red_colour
    roulette.input_bet_amount.send_keys('1e2')
    roulette.input_bet_amount.click()
    assert roulette.input_border_colour.get_css_value('border-color') == RouletteResources.grey_colour
