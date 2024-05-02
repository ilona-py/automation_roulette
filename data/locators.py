from selenium.webdriver.common.by import By


class RouletteLocators:
    justify_center_txt = (By.XPATH, "//*[@class='flex justify-center']//div[contains(@class, 'break-words')]")
    justify_center_button = (By.XPATH, "//*[@class='flex justify-center']//button")
    justify_center = (By.XPATH, "//*[@class='flex justify-center']")
    bets_block = (By.XPATH, "//div[contains(@class, 'bet-input__controls')]//button")
    input_bet_amount = (By.XPATH, "//div[@class='relative']//input")
    input_border_colour = (By.XPATH, "//div[@class='relative']//input//..")
    previous_rolls = (By.XPATH, "(//*[contains(@class, 'flex-col items-center')]//a)[1]")
    roll_history_title = (By.XPATH, '//h3')
    last_100 = (By.XPATH, "(//*[@class='label mr-2'])[1]")
    three_numers_of_100 = (By.XPATH,
                           "(//*[@class='flex items-center justify-end']//div[contains(@class, 'text-xxs')])[position() <= 3]")
    clear_button = (By.XPATH, "//div[contains(@class, 'bet-input__controls')]//button[contains(text(), 'Clear')]")


