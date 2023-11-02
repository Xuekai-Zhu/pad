def solution():
    regular_croissant_price = 3.5
    almond_croissant_price = 5.5
    num_saturdays = 52
    num_sundays = 52

    # Calculate the total amount spent on regular croissants in a year
    total_regular_croissant_cost = num_saturdays * regular_croissant_price

    # Calculate the total amount spent on almond croissants in a year
    total_almond_croissant_cost = num_sundays * almond_croissant_price

    # Calculate the total amount spent on croissants in a year
    total_cost = total_regular_croissant_cost + total_almond_croissant_cost
    result = total_cost
    return result

print(solution())