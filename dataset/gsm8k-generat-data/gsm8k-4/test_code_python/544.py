def solution():
    """Elise is buying more dog food. She buys a 15kg bag then another 10kg bag, and she now has 40kg of dog food. How many kilograms of dog food did Elise already have?"""
    # Calculate the total amount of dog food Elise has now
    total_dog_food = 40

    # Calculate the amount of dog food Elise bought
    bought_dog_food = 15 + 10

    # Calculate the amount of dog food Elise had before buying more
    initial_dog_food = total_dog_food - bought_dog_food

    # Return the result
    result = initial_dog_food
    return result

print(solution())