import allure
from data import RouletteResources


@allure.title("Verify 'Last 100' items block | Test Case 8")
def test_last_100(roulette, open_roulette):
    assert roulette.last_100.text == RouletteResources.last_100
    numbers = []
    for element in roulette.three_numers_of_100.find_elements():
        numbers.append(int(element.text))
    assert sum(numbers) == 100
