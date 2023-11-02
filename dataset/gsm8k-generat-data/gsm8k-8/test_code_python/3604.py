def solution():
    # Calculate the amount of food donated in the second week
    donated_food_week2 = 2 * 40

    # Calculate the total amount of food donated
    total_donated_food = 40 + donated_food_week2

    # Calculate the amount of food given out to the homeless
    food_given_out = 0.7 * total_donated_food

    # Calculate the amount of food remaining in the food bank
    food_remaining = total_donated_food - food_given_out
    result = food_remaining
    return result

print(solution())