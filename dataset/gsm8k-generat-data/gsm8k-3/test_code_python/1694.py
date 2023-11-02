def solution():
    """Carson is a night security guard. He's supposed to patrol the outside of a warehouse that's 600 feet long and 400 feet wide. If Carson is supposed to circle the warehouse 10 times, but gets tired and skips 2 times, how far does he walk in one night?"""
    # Calculate the perimeter of the warehouse
    perimeter = 2 * (600 + 400)

    # Calculate the distance Carson walks in one circle
    distance_per_circle = perimeter

    # Calculate the total distance Carson is supposed to walk
    total_distance = distance_per_circle * 10

    # Adjust for times skipped
    total_distance -= distance_per_circle * 2

    # Display the total distance Carson walks in one night
    result = total_distance
    return result

print(solution())