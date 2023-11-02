def solution():
    # Define the total number of donuts in the box
    total_donuts = 50

    # Subtract the donuts Bill ate on the way to work
    total_donuts -= 2

    # Subtract the donuts the secretary took
    total_donuts -= 4

    # Subtract the donuts his coworkers took
    total_donuts -= total_donuts / 2

    result = total_donuts
    return result

print(solution())