def solution():
    # Define Emma's time to run one arena
    emma_time_one_arena = 20 / 2

    # Define Fernando's time to run one arena
    fernando_time_one_arena = 2 * emma_time_one_arena

    # Calculate the total time for both of them to run all around two arenas
    total_time = emma_time_one_arena + fernando_time_one_arena

    result = total_time
    return result

print(solution())