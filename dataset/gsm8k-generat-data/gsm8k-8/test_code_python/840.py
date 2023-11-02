def solution():
    # Define the number of puppies and dogs
    num_puppies = 4
    num_dogs = 3

    # Calculate the amount of food a puppy eats in a day
    puppy_food_per_day = (3 * 2) / num_puppies

    # Calculate the amount of food a dog eats in a day
    dog_food_per_day = 4 * 3

    # Calculate the total amount of food the puppies eat in a day
    total_puppy_food_per_day = num_puppies * puppy_food_per_day

    # Calculate the total amount of food the dogs eat in a day
    total_dog_food_per_day = num_dogs * dog_food_per_day

    # Calculate the total amount of food all the animals eat in a day
    total_food_per_day = total_puppy_food_per_day + total_dog_food_per_day
    
    result = total_food_per_day
    return result

print(solution())