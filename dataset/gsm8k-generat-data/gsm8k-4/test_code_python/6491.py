def solution():
    """James gets a cable program. The first 100 channels cost $100 and the next 100 channels cost half that much. He splits it evenly with his roommate. How much did he pay?"""
    # Define the cost of the first 100 channels and the cost of the next 100 channels
    first_100_channels_cost = 100
    next_100_channels_cost = first_100_channels_cost / 2

    # Calculate the total cost of the cable program
    total_cost = (first_100_channels_cost + next_100_channels_cost)

    # Calculate how much James paid (split evenly with his roommate)
    james_paid = total_cost / 2

    # return the result
    result = james_paid
    return result

print(solution())