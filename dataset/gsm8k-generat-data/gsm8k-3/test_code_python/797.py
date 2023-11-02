def solution():
    """Hannah has three dogs. The first dog eats 1.5 cups of dog food a day. The second dog eats twice as much while the third dog eats 2.5 cups more than the second dog. How many cups of dog food should Hannah prepare in a day for her three dogs?"""
    # Define the amount of food each dog eats per day
    dog1_food = 1.5
    dog2_food = dog1_food * 2
    dog3_food = dog2_food + 2.5

    # Calculate the total amount of food needed per day for all three dogs
    total_food = dog1_food + dog2_food + dog3_food

    # Display the total amount of food needed per day for all three dogs
    result = total_food
    return result

print(solution())