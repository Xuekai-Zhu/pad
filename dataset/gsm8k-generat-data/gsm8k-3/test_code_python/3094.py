def solution():
    """Gina can paint six cups an hour with roses and 7 cups an hour with lilies. Her Etsy store gets an order for 6 rose cups and 14 lily cups. If Gina gets paid $90 total for the order, how much does she make per hour?"""
    # Define the number of cups painted per hour
    ROSE_RATE = 6
    LILY_RATE = 7

    # Define the number of cups in the order
    rose_cups = 6
    lily_cups = 14

    # Calculate the number of hours it takes to paint the cups
    rose_hours = rose_cups / ROSE_RATE
    lily_hours = lily_cups / LILY_RATE
    total_hours = rose_hours + lily_hours

    # Calculate the hourly rate
    hourly_rate = 90 / total_hours

    # Display the hourly rate
    result = hourly_rate
    return result

print(solution())