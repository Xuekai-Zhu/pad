def solution():
    """Elroy decides to enter a walk-a-thon and wants to make sure he ties last year's winner's cash collection. Last year, walkers earned $4 a mile. This year walkers earn $2.75 a mile. If last year's winner collected $44, how many more miles will Elroy walk than last year's winner to collect the same amount of money?"""
    # Define the cash collection of last year's winner and the rate per mile for both years
    last_year_cash = 44
    last_year_rate = 4
    this_year_rate = 2.75

    # Calculate the number of miles walked by last year's winner
    last_year_miles = last_year_cash / last_year_rate

    # Calculate the number of miles Elroy needs to walk to tie last year's winner's cash collection
    elroy_miles = last_year_cash / this_year_rate - last_year_miles

    # return the result
    result = elroy_miles
    return result

print(solution())