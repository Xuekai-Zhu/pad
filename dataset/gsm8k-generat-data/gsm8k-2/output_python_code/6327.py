def solution():
    """James decides to buy two suits. The first is an off-the-rack suit which costs $300. The second is a tailored suit that costs three as much plus an extra $200 for tailoring. How much did he pay for both suits?"""
    off_rack_suit_cost = 300
    tailored_suit_cost = (3 * off_rack_suit_cost) + 200
    total_cost = off_rack_suit_cost + tailored_suit_cost
    result = total_cost
    return result

print(solution())