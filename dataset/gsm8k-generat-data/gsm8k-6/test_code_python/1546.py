def solution():
    # Calculate the total time taken to drive herself
    driving_time = 3*60 + 15  # convert 3 hours 15 minutes to minutes

    # Calculate the total time taken to take the airplane
    airplane_time = 10 + 20 + (driving_time/3) + 10  # 10 minutes to drive to airport, 20 minutes to board, 1/3 of driving time on airplane, 10 minutes to get off airplane

    # Calculate the time difference between driving and taking the airplane
    difference = driving_time - airplane_time

    # Convert the time difference to minutes
    difference_in_minutes = difference % 60 + (difference // 60) * 100

    result = difference_in_minutes
    return result

print(solution())