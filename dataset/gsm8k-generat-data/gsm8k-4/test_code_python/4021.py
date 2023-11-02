def solution():
    """Jake decides to go to the beach for a fun day. It is a 2-hour drive each way. He then spends 2.5 times at long as his total driving time. How much time does the trip take?"""
    # Define the duration of the round trip
    drive_time = 2
    round_trip = drive_time * 2

    # Calculate the total time spent at the beach
    beach_time = round_trip * 2.5

    # Calculate the total duration of the trip
    total_time = round_trip + beach_time

    # return the result
    result = total_time
    return result

print(solution())