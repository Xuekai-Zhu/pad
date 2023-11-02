def solution():
    # Define the hourly rate and number of hours worked per day
    hourly_rate = 60
    daily_hours = 3

    # Calculate the total number of hours worked
    total_hours = daily_hours * 14

    # Calculate the total cost of hiring the magician
    total_cost = hourly_rate * total_hours
    result = total_cost
    return result

print(solution())