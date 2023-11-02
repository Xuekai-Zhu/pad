def solution():
    # Calculate the cost of the rose bushes
    rose_bushes_cost = 20 * 150  # Each rose bush costs $150

    # Calculate the cost of the gardener
    gardener_cost = 30 * 5 * 4  # The gardener works for 5 hours a day for 4 days

    # Calculate the cost of the soil
    soil_cost = 100 * 5  # 100 cubic feet of soil sold for $5 per cubic foot

    # Calculate the total cost of the gardening project
    total_cost = rose_bushes_cost + gardener_cost + soil_cost
    result = total_cost
    return result

print(solution())