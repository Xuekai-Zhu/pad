def solution():
    # Define the time played on Wednesday and Thursday
    wed_thu_time = 2

    # Calculate the time played on Friday
    fri_time = wed_thu_time + 3

    # Calculate the total time played over the three days
    total_time = (wed_thu_time * 2) + fri_time

    # Calculate the average time played per day
    avg_time = total_time / 3
    result = avg_time
    return result

print(solution())