def solution():
    """James gets a cable program.  The first 100 channels cost $100 and the next 100 channels cost half that much.  He splits it evenly with his roommate.  How much did he pay?"""
    
    # Define the cost of the first 100 channels and the discount cost of the next 100 channels
    CHANNELS_COST_1 = 100
    CHANNELS_COST_2 = CHANNELS_COST_1 / 2

    # Define the number of channels of each type
    channels_1 = 100
    channels_2 = 100

    # Calculate the total cost of the channels
    total_cost = channels_1 * CHANNELS_COST_1 + channels_2 * CHANNELS_COST_2

    # Calculate James' share of the cost
    james_share = total_cost / 2

    # Display James' share of the cost
    result = james_share
    return result

print(solution())