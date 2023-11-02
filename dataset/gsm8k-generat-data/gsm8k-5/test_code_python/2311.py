def solution():
    dogs = 3  # Melody has three dogs
    food_per_dog_per_day = 1 / 2  # Each dog eats 1/2 of a pound of food twice a day
    food_per_day = dogs * food_per_dog_per_day * 2  # Melody needs to give this much food to her dogs every day
    food_per_week = food_per_day * 7  # Melody needs this much food for a week
    food_left = 30 - food_per_week  # Melody bought 30 pounds of dog food

    result = food_left
    return result

print(solution())