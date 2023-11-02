def solution():
    """Gretchen is a scuba diver. She likes to hunt for treasure on the ocean's floor, but when she finds something to keep, she must carry it back to the surface of the water to give it to her shipmate on the boat. She can only carry 3 objects at a time while she swims underwater. If she finds 17 objects underwater, what is the fewest number of trips to the surface of the water she must take to carry all 17 objects to the boat?"""
    # Define the number of objects Gretchen can carry at a time
    carry_capacity = 3

    # Define the total number of objects Gretchen needs to carry
    total_objects = 17

    # Calculate the number of trips needed to carry all the objects
    trips = total_objects // carry_capacity
    if total_objects % carry_capacity != 0:
        trips += 1

    # Return the result
    result = trips
    return result

print(solution())