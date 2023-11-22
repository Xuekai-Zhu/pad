def solution():
    
    # Define the time it takes James to read 3 pages before and to read 18 pages
    TIME_BEFORE_READING = 10
    PAGES_READ_BEFORE_BED = 3
    PAGES_READ_AFTER_SLEEP = 18

    # Calculate the time it takes James to read 18 pages before and after the sleep
    time_before_sleep = PAGES_READ_BEFORE_BED * TIME_BEFORE_READING
    time_after_sleep = PAGES_READ_AFTER_SLEEP * TIME_BEFORE_READING

    # Calculate the total time James spends reading
    total_time = time_before_sleep + time_after_sleep

    # Display the total time James spends reading
    result = total_time
    return result

print(solution())