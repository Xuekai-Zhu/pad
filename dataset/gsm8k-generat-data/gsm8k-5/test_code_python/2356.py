def solution():
    orange_cost = 12  # Total cost of 1 kg of oranges
    apple_cost = orange_cost / 2  # Apples are two times cheaper than oranges
    total_cost = orange_cost + apple_cost * 3  # Total cost of both fruits

    # Calculate the cost of 1 kg of apples
    apple_kg_cost = (total_cost - orange_cost) / 3
    result = apple_kg_cost
    return result

print(solution())