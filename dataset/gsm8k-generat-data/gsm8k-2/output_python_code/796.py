def solution():
    """Hannah has three dogs. The first dog eats 1.5 cups of dog food a day. The second dog eats twice as much while the third dog eats 2.5 cups more than the second dog. How many cups of dog food should Hannah prepare in a day for her three dogs?"""
    first_dog_food = 1.5
    second_dog_food = 2 * first_dog_food
    third_dog_food = second_dog_food + 2.5
    total_food = first_dog_food + second_dog_food + third_dog_food
    result = total_food
    return result

print(solution())