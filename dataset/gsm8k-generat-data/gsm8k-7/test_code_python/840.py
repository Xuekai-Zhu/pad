def solution():
    num_puppies = 4
    num_dogs = 3
    dog_food_per_meal = 4
    num_meals_per_day = 3

    # Calculate the amount of food each puppy eats per meal
    puppy_food_per_meal = dog_food_per_meal / 2

    # Calculate the number of meals each puppy eats per day
    num_puppy_meals_per_day = num_meals_per_day * 3

    # Calculate the total amount of food the puppies eat per day
    total_puppy_food_per_day = num_puppies * puppy_food_per_meal * num_puppy_meals_per_day

    # Calculate the total amount of food the dogs eat per day
    total_dog_food_per_day = num_dogs * dog_food_per_meal * num_meals_per_day

    # Calculate the total amount of food all the animals eat per day
    total_food_per_day = total_puppy_food_per_day + total_dog_food_per_day
    result = total_food_per_day
    return result

print(solution())