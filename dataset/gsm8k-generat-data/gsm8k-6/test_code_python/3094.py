def solution():
    # Calculate the total time it takes Gina to paint the cups
    time_rose_cups = 6 / 6  # 6 cups of roses takes 1 hour to paint
    time_lily_cups = 14 / 7  # 14 cups of lilies take 2 hours to paint
    total_time = time_rose_cups + time_lily_cups  # total time to paint cups

    # Calculate the amount Gina earns per hour
    hourly_rate = 90 / total_time
    result = hourly_rate
    return result

print(solution())