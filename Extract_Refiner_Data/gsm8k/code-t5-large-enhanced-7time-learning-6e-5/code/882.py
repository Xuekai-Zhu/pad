def solution():
    
    # Define the number of microphones the singer wants to arrange in pairs
    total_microphones = 50

    # Calculate the number of microphones that won't find any space
    no_space = total_microphones * 0.2

    # Calculate the number of pairs of microphones that can be arrangeed with the remaining microphones
    arrange_pairs = total_microphones - no_space

    # Display the number of pairs of microphones
    result = arrange_pairs
    return result

print(solution())