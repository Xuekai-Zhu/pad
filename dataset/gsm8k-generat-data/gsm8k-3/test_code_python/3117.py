def solution():
    """Mark hires a singer for 3 hours at $15 an hour.  He then tips the singer 20%.  How much did he pay?"""
    # Define the cost per hour and the number of hours
    COST_PER_HOUR = 15
    HOURS = 3

    # Calculate the total cost of hiring the singer
    singer_cost = COST_PER_HOUR * HOURS

    # Calculate the amount of the tip
    tip = singer_cost * 0.2

    # Calculate the total amount paid
    total_cost = singer_cost + tip

    # Display the total cost
    result = total_cost
    return result

print(solution())