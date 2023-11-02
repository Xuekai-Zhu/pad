def solution():
    """Betty bought 1 kg of oranges and 3 kg of apples. The total cost of oranges was $12. The apples were two times cheaper than the oranges. How much did Betty pay for 1 kg of apples?"""
    orange_cost = 12
    apple_cost = (orange_cost / 2) * 3
    cost_per_kg = (orange_cost + apple_cost) / 4
    apple_cost_per_kg = (apple_cost / 3)
    result = apple_cost_per_kg
    return result

print(solution())