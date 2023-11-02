def solution():
    """Josie received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    gift_money = 50
    cost_of_tape = 9
    num_of_tapes = 2
    cost_of_headphone = 25
    total_cost = (cost_of_tape * num_of_tapes) + cost_of_headphone
    money_left = gift_money - total_cost
    result = money_left
    return result

print(solution())