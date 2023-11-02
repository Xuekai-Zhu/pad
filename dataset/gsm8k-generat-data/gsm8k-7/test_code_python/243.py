def solution():
    start_time = 8
    end_time = 15

    # Calculate the total number of hours worked
    total_hours = end_time - start_time

    # Subtract the two-hour meeting from the total hours
    total_hours -= 2

    result = total_hours
    return result

print(solution())