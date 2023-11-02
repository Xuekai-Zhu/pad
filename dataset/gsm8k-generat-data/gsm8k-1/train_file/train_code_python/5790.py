def solution():
    """Elroy decides to enter a walk-a-thon and wants to make sure he ties last year's winner's cash collection. Last year, walkers earned $4 a mile. This year walkers earn $2.75 a mile. If last year's winner collected $44, how many more miles will Elroy walk than last year's winner to collect the same amount of money?"""
    last_year_winner_amount = 44
    last_year_winner_pay_per_mile = 4
    this_year_pay_per_mile = 2.75
    miles_needed = last_year_winner_amount / this_year_pay_per_mile
    miles_last_year_winner_walked = last_year_winner_amount / last_year_winner_pay_per_mile
    extra_miles_needed = miles_needed - miles_last_year_winner_walked
    result = extra_miles_needed
    return result

print(solution())