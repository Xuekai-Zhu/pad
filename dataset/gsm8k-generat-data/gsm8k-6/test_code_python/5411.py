def solution():
    # Let's say distance traveled by both car and train is d
    # Let's say speed of car is s, and speed of train is t
    # Time taken by car to travel d distance = 4.5 hours
    # Time taken by train to travel d distance = 4.5 + 2 hours

    # We know that distance = speed x time
    # Therefore, d = s x 4.5 (distance traveled by car)
    # And d = t x 6.5 (distance traveled by train, 4.5 hour by car + additional 2 hours)

    # Equating both, we get s x 4.5 = t x 6.5
    # Therefore, t = (4.5s) / 6.5

    # Total time taken by both car and train to cover d distance = time taken by car + time taken by train
    # Total time taken = 4.5 hours + (6.5s / 4.5 hours)

    total_time = 4.5 + (6.5/4.5)
    result = total_time
    return result

print(solution())