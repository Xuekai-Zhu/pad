def solution():
    """Betty bought 1 kg of oranges and 3 kg of apples. The total cost of oranges was $12. The apples were two times cheaper than the oranges. How much did Betty pay for 1 kg of apples?"""

    # Calculate the cost of 1 kg of oranges
    cost_oranges = 12

    # Calculate the total cost of the apples
    total_cost_apples = (3/1) * cost_oranges / 2

    # Calculate the cost of 1 kg of apples
    cost_apples = total_cost_apples / 3

    # Display the cost of 1 kg of apples
    result = cost_apples
    return result

print(solution())