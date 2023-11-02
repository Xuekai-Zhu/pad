def solution():
    """There are four lamps in Valerie's room. All of them are burnt out, so she needs to buy new light bulbs. She needs 3 small light bulbs and 1 large light bulb. She has $60 to spend. If small light bulbs cost $8 and large light bulbs cost $12, how much money will Valerie have left over?"""
    small_bulbs_needed = 3
    large_bulbs_needed = 1
    small_bulb_cost = 8
    large_bulb_cost = 12
    total_cost = (small_bulbs_needed * small_bulb_cost) + (large_bulbs_needed * large_bulb_cost)
    money_left = 60 - total_cost
    result = money_left
    return result

print(solution())