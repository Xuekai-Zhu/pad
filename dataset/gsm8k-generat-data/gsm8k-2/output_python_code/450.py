def solution():
    """John buys a box of 40 light bulbs. He uses 16 of them and then gives half of what is left to a friend. How many does he have left?"""
    total_bulbs = 40
    used_bulbs = 16
    remaining_bulbs = total_bulbs - used_bulbs
    friend_bulbs = remaining_bulbs / 2
    total_remaining = remaining_bulbs - friend_bulbs
    result = total_remaining
    return result

print(solution())