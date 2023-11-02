def solution():
    """Kerry is ready to celebrate his birthday and wants to have three cakes with his age in candles on each of them. Candles come in boxes of 12 and cost $2.5 a box. If the candles cost $5, how old is Kerry?"""
    # Define the cost per box and the total cost of candles
    COST_PER_BOX = 2.5
    TOTAL_COST = 5

    # Calculate the number of boxes of candles needed
    num_boxes = TOTAL_COST / COST_PER_BOX

    # Calculate the total number of candles needed
    total_candles = num_boxes * 12

    # Calculate Kerry's age
    age = total_candles / 3

    # Round the age to the nearest integer
    age = round(age)

    # Return the result
    result = age
    return result

print(solution())