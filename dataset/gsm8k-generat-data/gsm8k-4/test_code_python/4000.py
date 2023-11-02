def solution():
    """Jenny and Mark are throwing bottle caps. Jenny's bottlecap flies 18 feet straight, then bounces off a street light and flies another 1/3 of the distance it already went. Mark's bottle cap flies 15 feet forward, then bounces off a window and flies twice as far as it already did. How much further did Mark's bottle cap go than Jenny's?"""
    # Calculate the total distance Jenny's bottlecap travels
    jenny_distance = 18 + (1/3)*18

    # Calculate the total distance Mark's bottlecap travels
    mark_distance = 15 + 2*15

    # Calculate the difference in distance between the two bottlecaps
    difference = mark_distance - jenny_distance

    # Return the result
    result = difference
    return result

print(solution())