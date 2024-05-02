import allure
from data import RouletteResources


@allure.title('Verify justify center content | Test Case 1')
def test_justify_center_content(roulette, open_roulette):
    assert roulette.justify_center_txt.text == RouletteResources.justify_center_txt
    roulette.justify_center_button.visibility_of_element()
    assert roulette.justify_center_button.text == RouletteResources.got_it
    roulette.justify_center_button.click()
    roulette.justify_center.wait_until_stale()

