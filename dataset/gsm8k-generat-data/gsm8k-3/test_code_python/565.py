def solution():
    """Tracy, Michelle, and Kati take a road trip that is a total of 1000 miles. Tracy drives 20 miles more than twice Michelle, and Michelle drives 3 times the amount that Katie drives. How many miles does Michelle drive?"""
    # Define the total distance of the road trip
    total_distance = 1000

    # Define the distance driven by Katie
    katie_distance = x

    # Define the distance driven by Michelle
    michelle_distance = 3 * katie_distance

    # Define the distance driven by Tracy
    tracy_distance = 2 * michelle_distance + 20

    # Calculate the total distance driven
    total_driven_distance = katie_distance + michelle_distance + tracy_distance

    # Solve for katie_distance
    katie_distance = (total_distance - 20) / 7

    # Solve for michelle_distance
    michelle_distance = 3*katie_distance

    # Display the distance Michelle drives
    result = michelle_distance
    return result

print(solution())