def solution():
    research_time = 6  # James spends 6 months researching
    first_find_time = 2 * 12  # James spends 2 years (2 * 12 months) on his first find

    # Calculate the total time for the first artifact (research + discovery)
    first_total_time = research_time + first_find_time

    second_find_time = 3 * first_find_time  # James spends 3 times as long on his second find

    # Calculate the total time for the second artifact (research + discovery)
    second_total_time = (research_time * 3) + second_find_time

    # Calculate the total time for both artifacts
    total_time = first_total_time + second_total_time
    result = total_time
    return result

print(solution())