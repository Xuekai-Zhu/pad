def solution():
    """A shipping boat's crew consisted of 17 sailors, with five inexperienced sailors. Each experienced sailor was paid 1/5 times more than the inexperienced sailors. If the inexperienced sailors were paid $10 per hour for a 60-hour workweek, calculate the total combined monthly earnings of the experienced sailors."""
    # Define the number of experienced sailors
    experienced_sailors = 17 - 5

    # Define the hourly rate of inexperienced sailors
    inexperienced_rate = 10

    # Calculate the hourly rate of experienced sailors
    experienced_rate = inexperienced_rate * 1.2

    # Calculate the weekly earnings of inexperienced sailors
    inexperienced_earnings = 5 * inexperienced_rate * 60

    # Calculate the weekly earnings of experienced sailors
    experienced_earnings = experienced_sailors * experienced_rate * 60

    # Calculate the total combined monthly earnings of experienced sailors
    total_earnings = experienced_earnings * 4

    # Return the result
    result = total_earnings
    return result

print(solution())