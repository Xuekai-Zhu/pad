def solution():
    """Amber is trying to decide if she wants to spend her $7 on candy or chips. She decides to buy the thing that she can get the most of. The bags of candy cost $1 and contain 12 ounces each. The bags of chips are $1.40 and contain 17 ounces each. How many ounces does she get if she buys the item that gives her the most?"""
    candy_price = 1
    candy_weight = 12
    chips_price = 1.4
    chips_weight = 17
    max_weight = max(int((7 / candy_price)) * candy_weight, int((7 / chips_price)) * chips_weight)
    result = max_weight
    return result

print(solution())