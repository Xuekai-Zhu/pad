def solution():
    # Define the cost of one box of candles and the total cost
    cost_per_box = 2.5
    total_cost = 5

    # Calculate the number of boxes purchased
    boxes_purchased = total_cost / cost_per_box

    # Calculate the number of candles needed
    total_candles_needed = 3 * Kerry_age

    # Calculate the number of boxes needed
    boxes_needed = total_candles_needed / 12

    # Use the number of boxes purchased to find Kerry's age
    Kerry_age = boxes_purchased * 12 / 3
    result = Kerry_age
    return result

print(solution())