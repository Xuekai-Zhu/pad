def solution():
    starting_cows = 39
    cows_died_last_year = 25
    cows_sold_last_year = 6
    cows_added_this_year = 24
    cows_bought_this_year = 43
    cows_gifted_this_year = 8

    # Calculate the total number of cows at the end of last year
    total_cows_last_year = starting_cows - cows_died_last_year - cows_sold_last_year

    # Calculate the total number of cows at the end of this year
    total_cows_this_year = total_cows_last_year + cows_added_this_year + cows_bought_this_year + cows_gifted_this_year
    result = total_cows_this_year
    return result

print(solution())