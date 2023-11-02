def solution():
    # Let's assume Uma watched x videos
    # Ekon watched 17 less than Uma, so Ekon watched x - 17 videos
    # Kelsey watched 43 more than Ekon, so Kelsey watched (x - 17) + 43

    # Total number of videos watched = 411
    # x + (x-17) + ((x-17) + 43) = 411

    # Solving for x, we get:
    x = 147

    # Therefore, Kelsey watched (x-17)+43 = 173 videos
    result = 173
    return result

print(solution())