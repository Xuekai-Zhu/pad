def solution():
    """Gnuff charges a flat rate of $20 per tutoring session plus $7 per minute. The total amount paid for Gnuff for tutoring for one session is $146. How many minutes did Gnuff tutor for?"""
    # Define the flat rate and the cost per minute
    flat_rate = 20
    cost_per_minute = 7

    # Define the total cost of the session
    total_cost = 146

    # Calculate the cost of the minutes spent in the session
    minutes_cost = total_cost - flat_rate

    # Calculate the number of minutes spent in the session
    minutes = minutes_cost / cost_per_minute

    # Display the result
    result = minutes
    return result

print(solution())