def solution():
    """Janice gave all three dozens of pebbles from her trip to her friends. Each of her friends got 4 pebbles. How many friends received pebbles?"""
    pebbles = 36
    per_friend = 4
    total_friends = pebbles // per_friend
    result = total_friends
    return result

print(solution())