def solution():
    soldiers_first_side = 4000  # First side has 4000 soldiers
    soldiers_second_side = soldiers_first_side - 500  # Second side has 500 soldiers fewer than the first side
    food_per_soldier = 10  # Both sides need 10 pounds of food per soldier per day
    food_second_side = food_per_soldier - 2  # Second side gets 2 pounds less food per soldier per day

    # Calculate the total amount of pounds of food both sides are eating altogether every day.
    total_food = (soldiers_first_side * food_per_soldier) + (soldiers_second_side * food_second_side)
    result = total_food
    return result

print(solution())