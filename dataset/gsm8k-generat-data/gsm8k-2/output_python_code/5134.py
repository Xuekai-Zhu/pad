def solution():
    """Kerry is ready to celebrate his birthday and wants to have three cakes with his age in candles on each of them. Candles come in boxes of 12 and cost $2.5 a box. If the candles cost $5, how old is Kerry?"""
    candle_boxes_cost = 2.5
    total_candles_cost = 5
    total_candle_boxes = total_candles_cost / candle_boxes_cost
    total_candles = total_candle_boxes * 12
    kerry_age = total_candles / 3
    result = kerry_age
    return result

print(solution())