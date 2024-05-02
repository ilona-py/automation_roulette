base_url = 'https://csgoempire.com/'


class RouletteResources:
    url = f'{base_url}roulette'
    justify_center_txt = 'For the month of May, we’re hosting a 10,000 coin daily roulette race. Scroll down to see more.'
    # I would make justify_center_txt less hardcode (at least 'May' and '10.000').
    # So we don't have to change it every month. Maybe would take data from API. Or any other possible way.
    got_it = 'Got it'
    bets = ['CLEAR', '+ 0.01', '+ 0.1', '+ 1', '+ 10', '+ 100', '1/ 2', 'X 2', 'MAX']
    red_colour = 'rgb(255, 92, 92)'
    grey_colour = 'rgb(146, 147, 166)'
    previous_rolls = "PREVIOUS ROLLS"
    roll_history_title = 'ROLL HISTORY'
    last_100 = 'LAST 100'
