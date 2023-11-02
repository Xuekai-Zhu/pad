def solution():
    # Calculate the total amount of food needed by the first side
    side1_food = 4000 * 10

    # Calculate the total amount of food needed by the second side
    side2_food = (4000 - 500) * 8

    # Calculate the total amount of food needed by both sides
    total_food = side1_food + side2_food
    result = total_food
    return result

print(solution())