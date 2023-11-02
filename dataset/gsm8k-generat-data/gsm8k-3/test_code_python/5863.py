def solution():
    """Mary is making a spinach quiche. She takes 40 ounces of raw spinach and cooks it until it's 20% of its initial volume. If she mixes the spinach with 6 ounces of cream cheese and 4 ounces of eggs, what is the total volume of the quiche?"""
    # Calculate the volume of cooked spinach
    cooked_volume = 40 * 0.2

    # Calculate the total volume of the quiche
    total_volume = cooked_volume + 6 + 4

    # Display the total volume of the quiche
    result = total_volume
    return result

print(solution())