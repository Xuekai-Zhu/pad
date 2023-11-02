def solution():
    """Mary is making a spinach quiche. She takes 40 ounces of raw spinach and cooks it until it's 20% of its initial volume. If she mixes the spinach with 6 ounces of cream cheese and 4 ounces of eggs, what is the total volume of the quiche?"""
    initial_volume = 40
    final_volume = initial_volume * 0.2
    total_volume = final_volume + 6 + 4
    result = total_volume
    return result

print(solution())