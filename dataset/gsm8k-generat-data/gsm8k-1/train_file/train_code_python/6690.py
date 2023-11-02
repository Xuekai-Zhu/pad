def solution():
    """Amanda received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    gift_amount = 50
    tape_price = 9
    num_tapes = 2
    headphone_price = 25
    total_spent = (tape_price * num_tapes) + headphone_price
    money_left = gift_amount - total_spent
    result = money_left
    return result

print(solution())