def solution():
    # Define the information given
    num_dogs = 3
    avg_food_week = 15
    second_dog_food_week = 13 * 2

    # Calculate the total food consumption of all 3 dogs
    total_food_week = num_dogs * avg_food_week

    # Calculate the food consumption of the third dog
    third_dog_food_week = total_food_week - (13 + second_dog_food_week)

    result = third_dog_food_week
    return result

print(solution())