def solution():
    number_of_shells_collected = 10
    number_of_days = 6
    number_of_shells_given_away = 2
    total_number_of_shells = number_of_shells_collected * number_of_days - number_of_shells_given_away
    result = total_number_of_shells
    return result

print(solution())