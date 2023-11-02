def solution():
    """Jenny is trying to convince her cat to walk on a leash. The cat spends twenty minutes resisting. Then Jenny coaxes the cat to walk 64 feet at a rate of 8 feet/minute. How many minutes does this whole process take?"""
    # Define the time spent resisting
    resist_time = 20

    # Define the distance and rate of walking on the leash
    distance = 64
    rate = 8

    # Calculate the time it takes to walk the distance at the given rate
    walk_time = distance / rate

    # Calculate the total time of the process
    total_time = resist_time + walk_time

    # Display the total time
    result = total_time
    return result

print(solution())