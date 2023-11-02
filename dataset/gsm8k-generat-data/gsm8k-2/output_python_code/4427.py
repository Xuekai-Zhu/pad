def solution():
    """Rick took off on a road trip for the summer. He traveled to the first destination on his trip, and then from there, he traveled twice the distance to this second destination. The third point on his trip was 40 miles away, which was half the distance he traveled from the beginning to his first destination. The final destination took twice the amount of driving of all the other legs put together. How many miles in total did he travel across all the legs of the trip?"""
    # Let x be the distance from the beginning to the first destination
    x = 2 * 40  # since the third destination is half the distance of the first leg (x/2)
    # Distance from first to second destination is twice that of x
    y = 2 * x
    # Total distance covered until the third destination is x + y + 40
    # Final destination is twice the previous distance, so total distance is 2(x + y + 40) = 2x + 2y + 80
    total_distance = x + y + 40 + 2 * (x + y + 40)
    result = total_distance
    return result

print(solution())