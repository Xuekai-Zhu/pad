def solution():
    olympics_start_date = "August 8, 2008"
    yeltsin_death_date = "April 23, 2007"
    if olympics_start_date > yeltsin_death_date:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())