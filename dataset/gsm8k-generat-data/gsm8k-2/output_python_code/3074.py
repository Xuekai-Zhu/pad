def solution():
    """James is running a fundraiser selling candy bars. Each box has 10 candy bars in it. He sells 5 boxes. He sells each candy bar for $1.50 and buys each bar for $1. How much profit does he make from these sales?"""
    box_size = 10
    num_boxes = 5
    sell_price = 1.5
    cost_price = 1
    total_sell_price = box_size * num_boxes * sell_price
    total_cost_price = box_size * num_boxes * cost_price
    profit = total_sell_price - total_cost_price
    result = profit
    return result

print(solution())