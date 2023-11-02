def solution():
    num_boxes = 2
    box_cost = 2.5

    # Calculate the total cost of candles
    total_cost = num_boxes * box_cost

    # Determine how many candles are needed for three cakes
    num_candles = 3 * Kerry_age

    # Determine how many boxes of candles are needed
    num_boxes_needed = math.ceil(num_candles / 12)

    # Calculate the total cost of all boxes of candles needed
    total_cost_needed = num_boxes_needed * box_cost

    # Determine Kerry's age
    Kerry_age = num_candles/3

    result = Kerry_age
    return result

print(solution())