def solution():
    """Kerry is ready to celebrate his birthday and wants to have three cakes with his age in candles on each of them.
    Candles come in boxes of 12 and cost $2.5 a box. If the candles cost $5, how old is Kerry?"""
    cost_per_box = 2.5
    total_cost = 5
    boxes_of_candles = total_cost / cost_per_box
    candles_per_cake = 3 * 12
    total_candles_needed = candles_per_cake * 3
    age = total_candles_needed // boxes_of_candles
    result = age
    return result

print(solution())