def solution():
    """Martin rings the small bell 4 times more than 1/3 as often as the big bell. If he rings both of them a combined total of 52 times, how many times does he ring the big bell?"""
    # Let x be the number of times Martin rings the big bell
    # Then the number of times he rings the small bell is 4 + (1/3)x
    # We know that the total number of times he rings both bells is 52
    # So we can write the equation:
    # x + 4 + (1/3)x = 52
    # Multiplying both sides by 3, we get:
    # 3x + 12 + x = 156
    # Combining like terms, we get:
    # 4x + 12 = 156
    # Subtracting 12 from both sides, we get:
    # 4x = 144
    # Dividing both sides by 4, we get:
    # x = 36
    # Therefore, Martin rings the big bell 36 times.

    result = 36
    return result

print(solution())