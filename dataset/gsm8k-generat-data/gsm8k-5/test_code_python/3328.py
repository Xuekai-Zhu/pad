def solution():
    average_food_per_week = 15  # all 3 dogs eat an average of 15 pounds of food per week
    dog2_food_per_week = 13 * 2  # the second dog eats double the amount of the first dog
    total_food_for_2_dogs = (13 + dog2_food_per_week)  # total food consumed by the first two dogs
    total_food_for_all_dogs = average_food_per_week * 3  # total food consumed by all 3 dogs
    food_for_third_dog = total_food_for_all_dogs - total_food_for_2_dogs  # food consumed by the third dog

    result = food_for_third_dog
    return result

print(solution())