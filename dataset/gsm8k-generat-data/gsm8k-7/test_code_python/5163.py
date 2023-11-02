def solution():
    num_guinea_pigs = 3
    first_pig_food = 2
    second_pig_food = 2 * first_pig_food
    third_pig_food = second_pig_food + 3

    # Calculate the total amount of food needed for all guinea pigs
    total_food = num_guinea_pigs * (first_pig_food + second_pig_food + third_pig_food)
    result = total_food
    return result

print(solution())