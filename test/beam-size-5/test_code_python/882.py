def solution():
    
    # Define the number of microphones in the stage
    stage_microphones = 50

    # Calculate the number of microphones that won't find any space in after arrangement
    no_space_arrangement = stage_microphones * 0.2

    # Calculate the number of pairs of microphones that won't find any space in after arrangement
    pairs_of_space_arrangement = stage_microphones - no_space_arrangement

    # Display the number of pairs of microphones that won't find any space in after arrangement
    result = pairs_of_space_arrangement
    return result

print(solution())