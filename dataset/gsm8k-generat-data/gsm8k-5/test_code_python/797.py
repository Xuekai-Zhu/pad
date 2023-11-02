def solution():
    # Calculate the amount of dog food the first dog eats
    dog1_food = 1.5

    # Calculate the amount of dog food the second dog eats (twice as much as the first dog)
    dog2_food = 2 * dog1_food

    # Calculate the amount of dog food the third dog eats (2.5 cups more than the second dog)
    dog3_food = dog2_food + 2.5

    # Calculate the total amount of dog food Hannah needs to prepare in a day
    total_food = dog1_food + dog2_food + dog3_food
    result = total_food
    return result

print(solution())