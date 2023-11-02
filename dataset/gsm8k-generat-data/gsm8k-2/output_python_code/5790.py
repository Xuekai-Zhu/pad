def solution():
    """Elroy decides to enter a walk-a-thon and wants to make sure he ties last year's winner's cash collection. Last year, walkers earned $4 a mile. This year walkers earn $2.75 a mile. If last year's winner collected $44, how many more miles will Elroy walk than last year's winner to collect the same amount of money?"""
    last_year_winners_money = 44
    last_year_money_per_mile = 4
    this_year_money_per_mile = 2.75
    miles_to_tie_last_year_winner = last_year_winners_money / last_year_money_per_mile
    elroys_money_to_tie_last_year_winner = miles_to_tie_last_year_winner * this_year_money_per_mile
    elroys_miles_to_tie_last_year_winner = elroys_money_to_tie_last_year_winner / this_year_money_per_mile - miles_to_tie_last_year_winner
    result = elroys_miles_to_tie_last_year_winner
    return result

print(solution())