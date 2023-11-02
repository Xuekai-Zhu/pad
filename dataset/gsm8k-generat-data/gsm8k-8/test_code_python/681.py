def solution():
    # Define the number of audiobooks and their length
    num_audiobooks = 6
    audiobook_length = 30

    # Calculate the total length of all the audiobooks
    total_length = num_audiobooks * audiobook_length

    # Calculate the total time it took her to finish all the audiobooks
    time_to_finish = total_length / 2

    result = time_to_finish
    return result

print(solution())