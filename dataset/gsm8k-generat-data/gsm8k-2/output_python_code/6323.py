def solution():
    """Jack collects all his neighbors' recycling and sorts out the cans and bottles to return for the deposit. He gets 10 cents per bottle and 5 cents per can. If he recycled 80 bottles and made $15, how many cans did he recycle?"""
    bottle_price = 10
    can_price = 5
    total_bottle_price = bottle_price * 80
    total_recycling_price = 1500
    total_can_price = (total_recycling_price - total_bottle_price) / can_price
    result = total_can_price
    return result

print(solution())