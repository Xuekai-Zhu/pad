def solution():
    """Bob has to hire someone to fix his garden. A storm destroyed all 20 of his rose bushes. He decides to replant all the rose bushes.
    Each rose bush costs $150. He also needs to pay a gardener $30 an hour, 5 hours each day for 4 days.
    The final expense is 100 cubic feet of soil sold for $5 per cubic foot.
    How much did the entire gardening project cost?"""
    # Define the cost of each rose bush
    rose_bush_cost = 150

    # Calculate the cost of replanting all 20 rose bushes
    replanting_cost = rose_bush_cost * 20

    # Calculate the cost of hiring the gardener
    gardener_cost = 30 * 5 * 4

    # Calculate the cost of buying 100 cubic feet of soil
    soil_cost = 100 * 5

    # Calculate the total cost of the gardening project
    total_cost = replanting_cost + gardener_cost + soil_cost

    # Return the result
    result = total_cost
    return result

print(solution())