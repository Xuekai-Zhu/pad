def solution():
    cans_on_desk = 28  # number of half-empty soda cans on Jerry's desk
    cans_per_trip = 4  # number of cans Jerry can carry per trip
    time_to_drain_cans = 30  # time it takes Jerry to drain 4 cans
    time_for_round_trip = 10  # time it takes Jerry for a round trip to sink/recycling bin

    # Calculate the number of trips Jerry needs to make
    num_trips = cans_on_desk // cans_per_trip
    if cans_on_desk % cans_per_trip != 0:
        num_trips += 1

    # Calculate the total time it takes Jerry to throw away all the cans
    total_time = (num_trips * time_to_drain_cans) + (num_trips * 2 * time_for_round_trip)
    result = total_time
    return result

print(solution())