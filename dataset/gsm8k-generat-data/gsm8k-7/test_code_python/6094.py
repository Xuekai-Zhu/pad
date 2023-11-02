def solution():
    time_at_zoo = 130  # 2 hours and 10 minutes in minutes
    time_at_elephants = 13
    time_at_penguins = time_at_elephants * 8
    total_time_at_seals_and_penguins = time_at_zoo - time_at_elephants

    # Calculate the time spent at seals
    time_at_seals = total_time_at_seals_and_penguins / 9
    result = time_at_seals
    return result

print(solution())