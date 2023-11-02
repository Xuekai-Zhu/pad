def solution():
    tablespoons_per_tablet = 500 / 9
    grams_per_tablet = 500 / 1000
    hours_between_doses = 4
    hours_taking_tylenol = 12
    number_of_doses = hours_taking_tylenol / hours_between_doses
    total_grams = number_of_doses * grams_per_tablet
    result = total_grams
    return result

print(solution())