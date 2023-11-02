def solution():
    """Amanda received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    gift_money = 50
    cassette_tape_cost = 9
    headphone_cost = 25
    total_cost = (2 * cassette_tape_cost) + headphone_cost
    money_left = gift_money - total_cost
    result = money_left
    return result

print(solution())