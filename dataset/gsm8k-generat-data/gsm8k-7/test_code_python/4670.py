def solution():
    flagpole_length = 60

    # Calculate the distance the flag traveled when raised to the top of the flagpole
    distance_raised = flagpole_length

    # Calculate the distance the flag traveled when lowered to half-mast
    distance_lowered = flagpole_length / 2

    # Calculate the distance the flag traveled when raised back to the top of the flagpole
    distance_raised_again = flagpole_length / 2

    # Calculate the total distance the flag traveled
    total_distance = distance_raised + distance_lowered + distance_raised_again

    result = total_distance
    return result

print(solution())