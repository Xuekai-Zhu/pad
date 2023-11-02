def solution():
    """Jack collects all his neighbors' recycling and sorts out the cans and bottles to return for the deposit. He gets 10 cents per bottle and 5 cents per can. If he recycled 80 bottles and made $15, how many cans did he recycle?"""
    bottle_return = 0.10
    can_return = 0.05
    total_return = 15.0
    bottles_recycled = 80
    bottle_earnings = bottles_recycled * bottle_return
    can_earnings = total_return - bottle_earnings
    cans_recycled = int(can_earnings / can_return)
    result = cans_recycled
    
    return result

print(solution())