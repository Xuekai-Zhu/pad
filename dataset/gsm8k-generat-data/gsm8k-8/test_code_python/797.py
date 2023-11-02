def solution():
    # Define the amount of food each dog eats
    dog1_food = 1.5
    dog2_food = 2 * dog1_food
    dog3_food = dog2_food + 2.5

    # Calculate the total amount of food needed
    total_food = dog1_food + dog2_food + dog3_food
    result = total_food
    return result

print(solution())