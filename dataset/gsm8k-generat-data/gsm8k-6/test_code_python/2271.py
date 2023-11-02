def solution():
    # Calculate the number of runners that will participate this year
    last_year_runners = 200
    runners_this_year = last_year_runners * 2 - 40  # twice as many runners as last year, minus the 40 who didn't show up
    result = runners_this_year
    return result

print(solution())