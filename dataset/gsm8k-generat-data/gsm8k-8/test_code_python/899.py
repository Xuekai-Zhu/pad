def solution():
    # Define the number of hours worked in 10 days
    total_hours = 10 * 8

    # Calculate the number of chairs that can be built in 1 hour
    chairs_per_hour = 1/5

    # Calculate the total number of chairs that can be built in 10 days
    total_chairs = total_hours * chairs_per_hour
    result = total_chairs
    return result

print(solution())