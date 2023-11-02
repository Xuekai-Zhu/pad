def solution():
    """Jeremy saw 12 birds in their backyard and threw a stone at them, scaring away 1/3 of that number. A few minutes later, 20 more birds joined the fearless birds. How many birds are now in the backyard?"""
    initial_birds = 12
    scared_birds = initial_birds / 3
    remaining_birds = initial_birds - scared_birds
    new_birds = 20
    total_birds = remaining_birds + new_birds
    result = total_birds
    return result

print(solution())