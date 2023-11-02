def solution():
    # Calculate the total amount spent on pasture rental
    pasture_cost = 500 * 12

    # Calculate the total amount spent on food
    food_cost = 10 * 365

    # Calculate the total amount spent on riding lessons
    lesson_cost = 60 * 2 * 52

    # Calculate the total amount spent in a year
    total_cost = pasture_cost + food_cost + lesson_cost
    result = total_cost
    return result

print(solution())