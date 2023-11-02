def solution():
    # Calculate the amount of money Opal put into savings from her first win
    savings_first_win = 100/2

    # Calculate the amount of money Opal bet on her second race
    bet_second_race = 100/2

    # Calculate the amount of money Opal won from her second race
    winnings_second_race = (bet_second_race*1.6) - bet_second_race

    # Calculate the amount of money Opal put into savings from her second win
    savings_second_win = winnings_second_race/2

    # Calculate the total amount Opal put into savings
    total_savings = savings_first_win + savings_second_win

    result = total_savings
    return result

print(solution())