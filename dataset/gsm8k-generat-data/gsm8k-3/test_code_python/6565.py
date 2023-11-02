def solution():
    """Gnuff charges a flat rate of $20 per tutoring session plus $7 per minute. The total amount paid for Gnuff for tutoring for one session is $146. How many minutes did Gnuff tutor for?"""
    # Define the flat rate and cost per minute
    FLAT_RATE = 20
    COST_PER_MINUTE = 7

    # Define the total amount paid
    total_paid = 146

    # Calculate the minutes tutored
    minutes_tutored = (total_paid - FLAT_RATE) / COST_PER_MINUTE

    # Display the minutes tutored
    result = minutes_tutored
    return result

print(solution())