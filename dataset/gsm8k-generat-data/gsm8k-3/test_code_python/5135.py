def solution():
    """Kerry is ready to celebrate his birthday and wants to have three cakes with his age in candles on each of them. Candles come in boxes of 12 and cost $2.5 a box. If the candles cost $5, how old is Kerry?"""
    # Define the cost of a box of candles and the number of candles per box
    CANDLE_COST = 2.5
    CANDLES_PER_BOX = 12

    # Calculate the number of boxes of candles Kerry bought
    num_boxes = int(5/CANDLE_COST)

    # Calculate the total number of candles Kerry bought
    num_candles = num_boxes * CANDLES_PER_BOX

    # Calculate Kerry's age based on the number of candles he needs
    age = int(num_candles/3)

    # Display Kerry's age
    result = age
    return result

print(solution())