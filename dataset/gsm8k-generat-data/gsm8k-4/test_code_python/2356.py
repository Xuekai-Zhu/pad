def solution():
    """Betty bought 1 kg of oranges and 3 kg of apples. The total cost of oranges was $12. The apples were two times cheaper than the oranges. How much did Betty pay for 1 kg of apples?"""
    # Define the cost of oranges and the ratio of apple cost to orange cost
    orange_cost = 12
    apple_to_orange_ratio = 0.5

    # Calculate the total cost of apples
    apple_cost = (3 * orange_cost) * apple_to_orange_ratio

    # Calculate the cost of 1 kg of apples
    price_per_kg = apple_cost / 3

    return price_per_kg

print(solution())