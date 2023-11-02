def solution():
    days_in_week = 7
    # check if the number of days in a week is a prime number or not
    if days_in_week == 2 or days_in_week == 3 or days_in_week == 5 or days_in_week == 7:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())