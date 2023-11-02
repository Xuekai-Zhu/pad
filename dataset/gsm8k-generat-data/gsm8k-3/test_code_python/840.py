def solution():
    """There are 4 puppies and 3 dogs at a camp. Each dog eats twice as much food as a puppy, but each puppy eats three times as often as a dog. If a dog eats 4 pounds of food three times a day, what would be the total amount of food the dogs and puppies eat in a day?"""
    # Define the amount of food a dog eats per meal
    DOG_MEAL = 4 * 3

    # Calculate the amount of food each puppy eats per meal
    PUPPY_MEAL = DOG_MEAL / 2

    # Calculate the number of times each puppy eats per day
    PUPPY_TIMES = 3 * 3

    # Calculate the total amount of food the puppies eat in a day
    total_puppy_food = PUPPY_MEAL * PUPPY_TIMES * 4

    # Calculate the total amount of food the dogs eat in a day
    total_dog_food = DOG_MEAL * 3 * 3

    # Calculate the total amount of food all the animals eat in a day
    total_food = total_puppy_food + total_dog_food

    # Display the total amount of food
    result = total_food
    return result

print(solution())