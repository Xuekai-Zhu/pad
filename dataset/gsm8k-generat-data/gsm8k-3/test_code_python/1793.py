def solution():
    """It takes Dawn 2 hours to paint 1 watercolor painting.  She was recently commissioned to paint a series of 12 paintings.  Dawn will earn $3,600.00 for these 12 paintings.  How much money does Dawn make per hour?"""
    # Define the number of paintings and the total earnings
    PAINTINGS = 12
    EARNINGS = 3600

    # Calculate the total time taken to paint all the paintings
    total_time = 2 * PAINTINGS

    # Calculate Dawn's hourly rate
    hourly_rate = EARNINGS / total_time

    # Display Dawn's hourly rate
    result = hourly_rate
    return result

print(solution())