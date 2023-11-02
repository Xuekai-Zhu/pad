def solution():
    """Gretchen is a scuba diver.  She likes to hunt for treasure on the ocean's floor, but when she finds something to keep, she must carry it back to the surface of the water to give it to her shipmate on the boat.  She can only carry 3 objects at a time while she swims underwater.  If she finds 17 objects underwater, what is the fewest number of trips to the surface of the water she must take to carry all 17 objects to the boat?"""
    # Calculate the number of trips Gretchen needs to make
    trips = 17 // 3
    if 17 % 3 != 0:
        trips += 1

    # Display the number of trips
    result = trips
    return result

print(solution())