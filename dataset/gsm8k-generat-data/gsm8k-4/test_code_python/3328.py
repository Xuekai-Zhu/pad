def solution():
    """Arthur has 3 dogs. They eat an average of 15 pounds of food a week. One dog eats 13 pounds a week. The second eats double this. How much does the third dog eat a week?"""
    # Define the total amount of food the dogs eat per week
    total_food = 15 * 3

    # Define the amount of food the first and second dogs eat per week
    first_dog_food = 13
    second_dog_food = 2 * first_dog_food

    # Calculate the amount of food the third dog eats per week
    third_dog_food = total_food - first_dog_food - second_dog_food

    # Return the result
    result = third_dog_food
    return result

print(solution())