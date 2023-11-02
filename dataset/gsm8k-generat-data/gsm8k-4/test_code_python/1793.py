def solution():
    """It takes Dawn 2 hours to paint 1 watercolor painting. She was recently commissioned to paint a series of 12 paintings. Dawn will earn $3,600.00 for these 12 paintings. How much money does Dawn make per hour?"""
    # Define the total number of paintings and the time it takes to paint one painting
    total_paintings = 12
    time_per_painting = 2

    # Calculate the total time Dawn spent painting the series
    total_time = total_paintings * time_per_painting

    # Calculate Dawn's hourly rate
    hourly_rate = 3600 / total_time

    # Round the hourly rate to 2 decimal places
    result = round(hourly_rate, 2)
    return result

print(solution())