def solution():
    """Tracy, Michelle, and Kati take a road trip that is a total of 1000 miles. Tracy drives 20 miles more than twice Michelle, and Michelle drives 3 times the amount that Katie drives. How many miles does Michelle drive?"""
    total_distance = 1000
    # let x be the number of miles Kati drives
    x = total_distance / 10
    # Michelle drives three times the number of miles Kati drives
    michelle_distance = 3 * x
    # Tracy drives 20 miles more than twice the number of miles Michelle drives
    tracy_distance = 2 * michelle_distance + 20
    # the sum of their distances is the total distance of the road trip
    sum_distance = x + michelle_distance + tracy_distance
    # Michelle's distance is the difference between the sum and Tracy and Kati's distances
    michelle_distance = sum_distance - (x + tracy_distance)
    result = michelle_distance
    return result

print(solution())