def solution():
    # Calculate the total amount of food the dogs and puppies eat in a day
    puppy_food = (4 * 3) * (1/3)  # each puppy eats three times as often as a dog, so they eat 1/3 of what a dog eats
    dog_food = 3 * 4 * 2  # each dog eats twice as much food as a puppy
    total_food = (4 * puppy_food) + (3 * dog_food)  # total amount of food the dogs and puppies eat in a day
    result = total_food
    return result

print(solution())