def solution():
    # Define the total distance covered in kilometers
    distance = 10

    # Calculate the total time taken in minutes
    total_time = 20 + 30

    # Calculate the average time per kilometer in minutes
    time_per_km = total_time / distance

    # Convert the time per kilometer to seconds
    time_per_km_sec = time_per_km * 60

    result = time_per_km_sec
    return result

print(solution())