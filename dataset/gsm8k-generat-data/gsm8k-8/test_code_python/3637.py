def solution():
    # Calculate the number of trips Gretchen needs to make
    num_trips = 17 // 3

    # If there are any remaining objects, Gretchen will need to make an additional trip
    if 17 % 3 != 0:
        num_trips += 1

    result = num_trips
    return result

print(solution())