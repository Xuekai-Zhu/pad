def solution():
    """Mary is making a spinach quiche. She takes 40 ounces of raw spinach and cooks it until it's 20% of its initial volume. If she mixes the spinach with 6 ounces of cream cheese and 4 ounces of eggs, what is the total volume of the quiche?"""
    # Define the initial volume of spinach
    initial_volume = 40

    # Calculate the final volume of spinach after cooking
    final_volume = initial_volume * 0.2

    # Calculate the total volume of ingredients in the quiche
    total_volume = final_volume + 6 + 4

    # return the result
    result = total_volume
    return result

print(solution())