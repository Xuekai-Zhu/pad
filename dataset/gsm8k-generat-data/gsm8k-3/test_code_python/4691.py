def solution():
    """Jerry was contracted to work on a house by his neighbor Miss Stevie. The time it took him to fix the broken kitchen counter was three times longer than the time he took painting the house. He took 8 hours painting the house and then helped mow Miss Stevie's lawn, taking 6 hours. If he charged Miss Stevie $15 per hour of work, calculate the amount of money that Miss Stevie paid him."""
    # Define the hourly rate
    HOURLY_RATE = 15

    # Calculate the time it took to fix the kitchen counter
    kitchen_time = 8 * 3

    # Calculate the total hours worked
    total_hours = kitchen_time + 8 + 6

    # Calculate the total amount earned
    total_earned = total_hours * HOURLY_RATE

    # Display the total amount earned
    result = total_earned
    return result

print(solution())