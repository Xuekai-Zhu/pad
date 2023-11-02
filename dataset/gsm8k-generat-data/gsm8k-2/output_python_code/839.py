def solution():
    """There are 4 puppies and 3 dogs at a camp. Each dog eats twice as much food as a puppy, but each puppy eats three times as often as a dog. If a dog eats 4 pounds of food three times a day, what would be the total amount of food the dogs and puppies eat in a day?"""
    dog_food = 4 * 2 * 3 # amount of food a dog eats in a day
    puppy_food = dog_food / 2 * 3 # amount of food a puppy eats in a day
    total_dogs_food = 3 * dog_food # amount of food all dogs eat in a day
    total_puppies_food = 4 * puppy_food # amount of food all puppies eat in a day
    total_food = total_dogs_food + total_puppies_food # total amount of food all dogs and puppies eat in a day
    result = total_food
    return result

print(solution())