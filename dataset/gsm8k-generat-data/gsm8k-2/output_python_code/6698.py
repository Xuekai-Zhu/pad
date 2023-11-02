def solution():
    """Bob has to hire someone to fix his garden. A storm destroyed all 20 of his rose bushes. He decides to replant all the rose bushes. Each rose bush costs $150. He also needs to pay a gardener $30 an hour, 5 hours each day for 4 days. The final expense is 100 cubic feet of soil sold for $5 per cubic foot. How much did the entire gardening project cost?"""
    rose_bushes_cost = 150 * 20
    gardener_cost = 30 * 5 * 4
    soil_cost = 100 * 5
    total_cost = rose_bushes_cost + gardener_cost + soil_cost
    result = total_cost
    return result

print(solution())