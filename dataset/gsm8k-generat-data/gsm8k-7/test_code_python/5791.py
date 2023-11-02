def solution():
    last_year_winner_collection = 44
    last_year_walker_earnings = 4.0
    this_year_walker_earnings = 2.75

    # Calculate the number of miles the last year's winner walked
    last_year_winner_miles = last_year_winner_collection / last_year_walker_earnings

    # Calculate the amount of money Elroy needs to collect to tie last year's winner
    elroy_target_collection = last_year_winner_collection

    # Calculate the number of miles Elroy needs to walk to collect the target amount
    elroy_miles = elroy_target_collection / this_year_walker_earnings

    # Calculate the difference in miles between Elroy and last year's winner
    miles_difference = elroy_miles - last_year_winner_miles
    result = miles_difference
    return result

print(solution())