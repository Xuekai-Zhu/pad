def solution():
    """William left Missouri by 7:00 AM and arrived at his hometown by 8:00 PM. He had 3 stops of 25, 10 and 25 minutes respectively during the journey. How many hours did he spend on the road?"""
    # Define the time of departure and arrival in hours
    departure_time = 7.0
    arrival_time = 20.0

    # Calculate the total time spent on the road in minutes
    total_time = (arrival_time - departure_time) * 60 - 60 - 25 - 10 - 25

    # Convert the total time to hours
    total_hours = total_time / 60

    # Return the result
    result = total_hours
    return result

print(solution())