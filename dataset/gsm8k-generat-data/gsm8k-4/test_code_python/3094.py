def solution():
    """Gina can paint six cups an hour with roses and 7 cups an hour with lilies. Her Etsy store gets an order for 6 rose cups and 14 lily cups. If Gina gets paid $90 total for the order, how much does she make per hour?"""
    # Define the number of cups painted per hour for each type
    ROSE_CUPS_PER_HOUR = 6
    LILY_CUPS_PER_HOUR = 7

    # Define the number of cups in the order
    rose_cups = 6
    lily_cups = 14

    # Calculate the total time it takes to paint the order
    total_time = (rose_cups / ROSE_CUPS_PER_HOUR) + (lily_cups / LILY_CUPS_PER_HOUR)

    # Calculate how much Gina makes per hour
    hourly_earnings = 90 / total_time

    result = hourly_earnings
    return result

print(solution())