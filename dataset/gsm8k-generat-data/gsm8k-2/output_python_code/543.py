def solution():
    """Elise is buying more dog food. She buys a 15kg bag then another 10kg bag, and she now has 40kg of dog food. How many kilograms of dog food did Elise already have?"""
    total_dog_food = 40
    bought_dog_food = 15 + 10
    previous_dog_food = total_dog_food - bought_dog_food
    result = previous_dog_food
    return result

print(solution())