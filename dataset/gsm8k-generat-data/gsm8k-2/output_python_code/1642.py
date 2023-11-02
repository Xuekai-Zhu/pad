def solution():
    """There are four lamps in Valerie's room. All of them are burnt out, so she needs to buy new light bulbs. She needs 3 small light bulbs and 1 large light bulb. She has $60 to spend. If small light bulbs cost $8 and large light bulbs cost $12, how much money will Valerie have left over?"""
    small_bulb_price = 8
    large_bulb_price = 12
    small_bulb_count = 3
    large_bulb_count = 1
    total_price = (small_bulb_price * small_bulb_count) + (large_bulb_price * large_bulb_count)
    remaining_money = 60 - total_price
    result = remaining_money
    return result

print(solution())