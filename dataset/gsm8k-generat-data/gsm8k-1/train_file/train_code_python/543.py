def solution():
    """Elise is buying more dog food. She buys a 15kg bag then another 10kg bag, and she now has 40kg of dog food. How many kilograms of dog food did Elise already have?"""
    bag1_weight = 15
    bag2_weight = 10
    total_weight = 40
    initial_weight = total_weight - (bag1_weight + bag2_weight)
    result = initial_weight
    return result

print(solution())