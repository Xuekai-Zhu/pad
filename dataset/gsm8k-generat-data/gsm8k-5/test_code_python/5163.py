def solution():
    # Calculate the amount of food each guinea pig needs
    food_needed_guinea_pig_1 = 2
    food_needed_guinea_pig_2 = 2 * food_needed_guinea_pig_1
    food_needed_guinea_pig_3 = food_needed_guinea_pig_2 + 3

    # Calculate the total amount of food needed
    total_food_needed = food_needed_guinea_pig_1 + food_needed_guinea_pig_2 + food_needed_guinea_pig_3
    result = total_food_needed
    return result

print(solution())