def solution():
    # Calculate the yearly cost of renting the pasture
    pasture_cost = 500 * 12

    # Calculate the yearly cost of feeding the pony
    food_cost = 10 * 365

    # Calculate the yearly cost of lessons
    lesson_cost = 60 * 2 * 52

    # Calculate the total yearly cost
    total_cost = pasture_cost + food_cost + lesson_cost

    result = total_cost
    return result

print(solution())