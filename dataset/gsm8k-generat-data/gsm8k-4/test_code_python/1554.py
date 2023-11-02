def solution():
    """Jerry has a bunch of half-empty soda cans on his desk. He needs to drain all of them and put them in the recycling bin. He can carry four cans at once, and it takes him 30 seconds to drain those 4 cans. It takes him ten seconds each way to walk to the sink and recycling bin and then back to his desk. If there are 28 cans on Jerry's desk, how long does it take him to throw all of them away?"""
    # Define the number of cans Jerry has and the number of trips he needs to make
    cans = 28
    trips = int(cans / 4)

    # Define how long it takes Jerry to drain the cans and make a trip
    drain_time = 30
    trip_time = 10

    # Calculate how long it takes Jerry to throw away all the cans
    total_time = (trips * drain_time) + (trips * trip_time)

    # If there are any remaining cans, add the time it takes to drain them and make a final trip to the total time
    remaining_cans = cans % 4
    if remaining_cans > 0:
        total_time += drain_time
        total_time += trip_time

    # Convert the time to minutes and seconds
    minutes = total_time // 60
    seconds = total_time % 60

    # Return the result in the format of MM:SS
    result = f"{minutes:02d}:{seconds:02d}"
    return result

print(solution())