def solution():
    """Arthur has 3 dogs. They eat an average of 15 pounds of food a week. One dog eats 13 pounds a week. The second eats double this. How much does the third dog eat a week?"""
    # Define the average weekly food consumption of 3 dogs and the food consumption of 2 dogs
    AVERAGE_CONSUMPTION = 15
    TWO_DOG_CONSUMPTION = 26 # 13 * 2

    # Define the food consumption of the first 2 dogs and calculate the food consumption of the third dog
    first_dog_consumption = 13
    second_dog_consumption = 26 # double the first dog's consumption
    third_dog_consumption = (AVERAGE_CONSUMPTION * 3) - (first_dog_consumption + second_dog_consumption)

    # Display the food consumption of the third dog
    result = third_dog_consumption
    return result

print(solution())