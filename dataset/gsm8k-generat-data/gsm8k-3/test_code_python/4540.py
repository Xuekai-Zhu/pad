def solution():
    """Tracy feeds each of her two dogs 1.5 cups of food per meal. She feeds her dogs thrice a day. How many pounds of food do her two dogs consume if 1 pound is equal to 2.25 cups?"""
    # Define the cups of food each dog eats per day
    cups_per_dog = 1.5 * 3

    # Calculate the total cups of food for both dogs
    total_cups = cups_per_dog * 2

    # Convert cups to pounds
    pounds = total_cups / 2.25

    # Display the total pounds of food consumed
    result = pounds
    return result

print(solution())