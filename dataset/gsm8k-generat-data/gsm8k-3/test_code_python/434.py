def solution():
    """Calvin has been saving his hair clippings after each haircut to make a wig for his dog. He has gotten 8 haircuts and knows that he needs 2 more to reach his goal. What percentage towards his goal is he?"""
    # Define the number of haircuts Calvin has gotten and needs to reach his goal
    haircuts_gotten = 8
    haircuts_needed = 2

    # Calculate the percentage of haircuts Calvin has gotten towards his goal
    percentage_complete = (haircuts_gotten / (haircuts_gotten + haircuts_needed)) * 100

    # Display the percentage complete
    result = percentage_complete
    return result

print(solution())