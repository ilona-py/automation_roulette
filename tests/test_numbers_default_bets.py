import allure
from data import RouletteResources


@allure.title('Verify numbers of default bets | Test Case 3')
def test_numbers_of_default_bets(roulette, open_roulette):
    assert roulette.bets_block.visibility_of_element()
    bets = []
    for element in roulette.bets_block.find_elements():
        bets.append(element.text)
    assert bets == RouletteResources.bets
