def solution():
    gestation_period = 135 # minimum number of days for a markhor
    days_in_year = 365
    possible_births = days_in_year // gestation_period # number of times a markhor can give birth in a year
    if possible_births >= 3:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())