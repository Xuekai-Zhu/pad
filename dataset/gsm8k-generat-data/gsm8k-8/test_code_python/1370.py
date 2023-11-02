def solution():
    # Define the initial number of strands and the cutting rates
    initial_strands = 22
    hannah_rate = 8
    son_rate = 3

    # Calculate the time it takes for Hannah to cut all her strands
    hannah_time = initial_strands / hannah_rate

    # Calculate the number of remaining strands for the son to cut
    remaining_strands = initial_strands - hannah_time * hannah_rate

    # Calculate the time it takes for the son to cut the remaining strands
    son_time = remaining_strands / son_rate

    # Calculate the total time
    total_time = hannah_time + son_time
    result = total_time
    return result

print(solution())