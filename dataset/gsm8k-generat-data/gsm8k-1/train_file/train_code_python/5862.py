def solution():
    """Mary is making a spinach quiche. She takes 40 ounces of raw spinach and cooks it until it's 20% of its initial volume. If she mixes the spinach with 6 ounces of cream cheese and 4 ounces of eggs, what is the total volume of the quiche?"""
    initial_spinach = 40
    cooked_spinach = initial_spinach * 0.2
    total_volume = cooked_spinach + 6 + 4
    result = total_volume
    return result

print(solution())