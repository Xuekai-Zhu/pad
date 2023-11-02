def solution():
    """Mark hires a singer for 3 hours at $15 an hour. He then tips the singer 20%. How much did he pay?"""
    # Define the hourly rate and the number of hours worked
    HOURLY_RATE = 15
    HOURS_WORKED = 3

    # Calculate the cost of hiring the singer
    base_cost = HOURLY_RATE * HOURS_WORKED

    # Calculate the tip amount
    tip = 0.2 * base_cost

    # Add the tip to the base cost to get the total amount paid
    total_paid = base_cost + tip

    result = total_paid
    return result

print(solution())