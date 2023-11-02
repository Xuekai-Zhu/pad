def solution():
    """Jerry has a bunch of half-empty soda cans on his desk. He needs to drain all of them and put them in the recycling bin. He can carry four cans at once, and it takes him 30 seconds to drain those 4 cans. It takes him ten seconds each way to walk to the sink and recycling bin and then back to his desk. If there are 28 cans on Jerry's desk, how long does it take him to throw all of them away?"""
    # Define the number of cans Jerry has and the time it takes to drain 4 cans
    num_cans = 28
    drain_time = 30

    # Define the time it takes Jerry to walk to the sink and recycling bin and back to his desk
    round_trip_time = 10 * 2

    # Calculate the number of trips Jerry needs to make
    num_trips = num_cans // 4
    if num_cans % 4 != 0:
        num_trips += 1

    # Calculate the total time it takes Jerry to throw away all the cans
    total_time = num_trips * (drain_time + round_trip_time)

    # Display the total time
    result = total_time
    return result

print(solution())