def solution():
    """John went on a mission that was supposed to take 5 days. Instead it took 60% longer. He then had to go on a second mission which took 3 days. How long was he on missions?"""
    # Calculate the additional time for the first mission
    additional_time = 5 * 0.6

    # Calculate the total time for the first mission
    total_time_first = 5 + additional_time

    # Calculate the total time for both missions
    total_time = total_time_first + 3

    result = total_time
    return result

print(solution())