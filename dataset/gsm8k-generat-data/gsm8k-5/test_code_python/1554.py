def solution():
    cans_on_desk = 28  # There are 28 cans on Jerry's desk
    cans_per_trip = 4  # Jerry can carry 4 cans at once
    time_per_trip = 10  # It takes Jerry 10 seconds each way to walk to the sink and recycling bin

    # Calculate the number of trips Jerry needs to make to throw away all the cans
    trips = (cans_on_desk + 3) // 4  # Round up to the nearest integer

    # Calculate the total time it takes Jerry to throw away all the cans
    total_time = trips * (cans_per_trip * 30 + time_per_trip * 2)

    result = total_time
    return result

print(solution())