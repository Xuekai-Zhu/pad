def solution():
    total_distance = 1000  # The road trip is a total of 1000 miles
    kati_distance = total_distance / 10  # Kati drives 1/10 of the total distance
    michelle_distance = 3 * kati_distance  # Michelle drives 3 times the distance that Kati drives
    tracy_distance = (2 * michelle_distance) + 20  # Tracy drives 20 more than twice Michelle's distance

    # Calculate Michelle's distance
    michelle_distance = total_distance - kati_distance - tracy_distance
    result = michelle_distance
    return result

print(solution())