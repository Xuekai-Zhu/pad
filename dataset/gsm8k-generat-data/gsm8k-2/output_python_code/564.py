def solution():
    """Tracy, Michelle, and Kati take a road trip that is a total of 1000 miles. Tracy drives 20 miles more than twice Michelle, and Michelle drives 3 times the amount that Katie drives. How many miles does Michelle drive?"""
    total_distance = 1000
    katie_distance = x
    michelle_distance = 3 * katie_distance
    tracy_distance = 20 + 2* michelle_distance

    # total distance is the sum of distances driven by all three
    total_distance_driven = tracy_distance + michelle_distance + katie_distance

    # we know total distance so we can find Michelle's distance
    michelle_distance = (total_distance - katie_distance - tracy_distance) / 3

    result = michelle_distance
    return result

print(solution())