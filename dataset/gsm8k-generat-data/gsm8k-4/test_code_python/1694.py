def solution():
    """Carson is a night security guard. He's supposed to patrol the outside of a warehouse that's 600 feet long and 400 feet wide. If Carson is supposed to circle the warehouse 10 times, but gets tired and skips 2 times, how far does he walk in one night?"""
    # Define the dimensions of the warehouse
    length = 600
    width = 400

    # Calculate the perimeter of the warehouse
    perimeter = 2 * (length + width)

    # Calculate the distance Carson walks in one full patrol
    total_distance = perimeter * 10

    # Calculate the distance Carson walks in one night
    actual_distance = total_distance - perimeter * 2

    result = actual_distance
    return result

print(solution())