def solution():
    # Define the start and end times for each work session
    start1 = 8
    end1 = 11
    start2 = 13
    end2 = 15

    # Calculate the total time Mckenna spends at work
    total_time = (end1 - start1) + (end2 - start2)

    # Convert the total time to hours
    total_hours = total_time / 100

    result = total_hours
    return result

print(solution())