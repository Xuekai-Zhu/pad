def solution():
    num_people = 3
    num_cups_per_person_per_day = 2
    ounces_per_cup = 0.5
    cost_per_ounce = 1.25
    num_days = 7

    # Calculate the total number of cups of coffee consumed in a week
    total_cups_per_day = num_people * num_cups_per_person_per_day
    total_cups_per_week = total_cups_per_day * num_days

    # Calculate the total amount of coffee needed in a week (in ounces)
    total_ounces_per_week = total_cups_per_week * ounces_per_cup

    # Calculate the total cost of the coffee for the week
    total_cost = total_ounces_per_week * cost_per_ounce
    result = total_cost
    return result

print(solution())