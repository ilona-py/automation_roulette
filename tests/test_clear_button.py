import allure


@allure.title("Verify the functionality of the 'Clear' button in the bet amount field | Test Case 11")
def test_clear_button(roulette, open_roulette):
    random_nmb = '19'  # here could be some randomizer function
    roulette.input_bet_amount.send_keys(random_nmb)
    assert roulette.input_bet_amount.get_value() == random_nmb
    roulette.clear_button.click()
    assert roulette.input_bet_amount.get_value() == '0'
