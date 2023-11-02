def solution():
    flagpole_length = 60  # The flagpole is 60 feet long

    # Calculate the distance covered by the flag when raised to the top of the pole
    distance_raised = flagpole_length

    # Calculate the distance covered by the flag when lowered to half-mast
    distance_lowered = flagpole_length / 2

    # Calculate the distance covered by the flag when raised to the top of the pole a second time
    distance_raised_twice = flagpole_length / 2

    # Calculate the total distance covered by the flag in one day
    total_distance = distance_raised + distance_lowered + distance_raised_twice
    result = total_distance
    return result

print(solution())