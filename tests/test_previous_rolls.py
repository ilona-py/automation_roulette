import allure
from data import RouletteResources


@allure.title('Verify "Previous Rolls" | Test Case 7')
def test_previous_rolls(roulette, open_roulette):
    assert roulette.previous_rolls.text == RouletteResources.previous_rolls
    roulette.previous_rolls.click()
    roulette.wait_page_loaded()
    assert roulette.roll_history_title.text == RouletteResources.roll_history_title
