def solution():
    num_people = 6  # Brian, his wife, 2 kids, and 2 parents
    servings_per_person = 2
    ml_per_cup = 250
    cups_per_serving = 0.5
    servings_total = num_people * servings_per_person

    # Calculate the total amount of milk needed in ml
    ml_total = servings_total * cups_per_serving * ml_per_cup

    # Calculate the number of 1L cartons needed
    cartons_needed = ml_total / 1000

    result = cartons_needed
    return result

print(solution())