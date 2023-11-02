def solution():
    number_of_puppies = 4
    number_of_dogs = 3
    multiplier_for_dogs = 2
    multiplier_for_puppies = 3
    pounds_of_food_per_day_for_a_dog = 4
    total_pounds_of_food_per_day_for_a_dog = pounds_of_food_per_day_for_a_dog * number_of_dogs * multiplier_for_dogs
    total_pounds_of_food_per_day_for_a_puppy = pounds_of_food_per_day_for_a_dog / multiplier_for_dogs * number_of_puppies * multiplier_for_puppies
    total_amount_of_food = total_pounds_of_food_per_day_for_a_puppy + total_pounds_of_food_per_day_for_a_dog
    result = total_amount_of_food
    
    return result

print(solution())