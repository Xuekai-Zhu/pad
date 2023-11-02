def solution():
    """There are 4 puppies and 3 dogs at a camp. Each dog eats twice as much food as a puppy, but each puppy eats three times as often as a dog. If a dog eats 4 pounds of food three times a day, what would be the total amount of food the dogs and puppies eat in a day?"""
    num_puppies = 4
    num_dogs = 3
    puppy_food_ratio = 1
    dog_food_ratio = 2
    puppy_frequency_ratio = 3
    dog_frequency_ratio = 1
    total_puppy_food = num_puppies * puppy_food_ratio * puppy_frequency_ratio
    total_dog_food = num_dogs * dog_food_ratio * dog_frequency_ratio * 4
    total_food = total_puppy_food + total_dog_food
    result = total_food
    return result

print(solution())