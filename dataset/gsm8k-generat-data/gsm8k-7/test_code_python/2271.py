def solution():
    last_year_sign_up = 200
    no_show = 40
    this_year_multiplier = 2

    # Calculate the number of people who actually ran last year
    actual_runners = last_year_sign_up - no_show

    # Calculate the number of runners this year
    this_year_runners = actual_runners * this_year_multiplier
    result = this_year_runners
    return result

print(solution())