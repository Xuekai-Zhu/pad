def solution():
    """Elise is buying more dog food. She buys a 15kg bag then another 10kg bag, and she now has 40kg of dog food. How many kilograms of dog food did Elise already have?"""
    # Define the weight of the bags she bought
    bag1_weight = 15
    bag2_weight = 10

    # Calculate the total weight of the bags bought
    total_bags_weight = bag1_weight + bag2_weight

    # Calculate the weight of the dog food she already had
    elise_dog_food_weight = 40 - total_bags_weight

    # Display the weight of the dog food she already had
    result = elise_dog_food_weight
    return result

print(solution())