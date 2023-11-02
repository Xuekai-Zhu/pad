def solution():
    """Hannah has three dogs. The first dog eats 1.5 cups of dog food a day. The second dog eats twice as much while the third dog eats 2.5 cups more than the second dog. How many cups of dog food should Hannah prepare in a day for her three dogs?"""
    # Define the amount of food the first dog eats
    dog1_food = 1.5

    # Define the amount of food the second dog eats (twice as much as the first)
    dog2_food = 2 * dog1_food

    # Define the amount of food the third dog eats (2.5 cups more than the second)
    dog3_food = dog2_food + 2.5

    # Calculate the total amount of food needed for all three dogs
    total_food = dog1_food + dog2_food + dog3_food

    # Round the result to the nearest tenth
    result = round(total_food, 1)
    return result

print(solution())