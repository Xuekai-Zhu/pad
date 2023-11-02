def solution():
    # Find the total amount of food consumed by all three dogs per week
    total_food = 3 * 15  # average of 15 pounds of food a week for 3 dogs

    # Find the amount of food consumed by the second dog
    second_dog_food = 13 * 2  # double the amount of the first dog

    # Subtract the amounts consumed by the first and second dogs to find the amount consumed by the third dog
    third_dog_food = total_food - 13 - second_dog_food
    result = third_dog_food
    return result

print(solution())