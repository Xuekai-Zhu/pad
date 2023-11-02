def solution():
    """Tracy, Michelle, and Kati take a road trip that is a total of 1000 miles. Tracy drives 20 miles more than twice Michelle, and Michelle drives 3 times the amount that Katie drives. How many miles does Michelle drive?"""
    # Define the total distance of the road trip
    total_distance = 1000

    # Let x be the distance driven by Katie
    x = total_distance / 10

    # Calculate the distance driven by Michelle
    michelle_distance = 3 * x

    # Calculate the distance driven by Tracy
    tracy_distance = 2 * michelle_distance + 20

    # Calculate the total distance driven
    total_driven = michelle_distance + tracy_distance + x

    # Check that the total distance driven equals the total distance of the road trip
    if total_driven == total_distance:
        result = michelle_distance
    else:
        result = "Error: Total distance driven does not equal total distance of road trip"

    return result

print(solution())