def solution():
    """Rick took off on a road trip for the summer.  He traveled to the first destination on his trip, and then from there, he traveled twice the distance to this second destination.  The third point on his trip was 40 miles away, which was half the distance he traveled from the beginning to his first destination.  The final destination took twice the amount of driving of all the other legs put together.  How many miles in total did he travel across all the legs of the trip?"""
    # Let x be the distance from the start to the first destination
    # Then the distance from the first to the second destination is 2x
    # The third destination is 40 miles away and half the distance from the start to the first destination, so the distance from the start to the first destination is 80 miles
    x = 80

    # Calculate the distance for each leg of the trip
    leg1 = x
    leg2 = 2 * x
    leg3 = 40
    leg4 = 2 * (leg1 + leg2 + leg3)

    # Calculate the total distance of the trip
    total_distance = leg1 + leg2 + leg3 + leg4

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())