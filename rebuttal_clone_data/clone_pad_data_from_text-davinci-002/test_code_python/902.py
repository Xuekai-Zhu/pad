def solution():
    straws = 300
    adult_pigs = 3/5
    piglets = 1/5
    straws_ eaten_by_adult_pigs = adult_pigs * straws
    straws_left = straws - straws_eaten_by_adult_pigs
    number_of_piglets = 20
    straws_eaten_by_piglets = straws_left / number_of_piglets
    result = straws_eaten_by_piglets
    return result

print(solution())