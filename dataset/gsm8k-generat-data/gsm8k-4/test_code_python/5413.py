def solution():
    """Ben wants to pick 56 sugar snap peas. At his current rate of picking, all will be picked in seven minutes. How long, in minutes, would it take Ben to pick 72 sugar snap peas?"""
    # Define the current number of sugar snap peas and the time it takes to pick them
    current_peas = 56
    current_time = 7

    # Calculate the picking rate
    picking_rate = current_peas / current_time

    # Calculate the time it would take to pick 72 sugar snap peas
    new_peas = 72
    new_time = new_peas / picking_rate

    # Return the result
    result = new_time
    return result

print(solution())