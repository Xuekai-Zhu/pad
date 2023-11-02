def solution():
    # Calculate the number of trips required to carry 30 bags of groceries
    total_trips = 30 // (3 * 2) + (30 % (3 * 2) > 0)  # divide the total number of bags by the number of bags carried in one trip by both Elysse and her brother, and round up to the nearest integer
    result = total_trips
    return result

print(solution())