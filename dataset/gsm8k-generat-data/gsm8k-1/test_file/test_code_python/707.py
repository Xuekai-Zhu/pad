def solution():
    """The ice cream parlor was offering a deal, buy 2 scoops of ice cream, get 1 scoop free. Each scoop cost $1.50. If Erin had $6.00, how many scoops of ice cream should she buy?"""
    price_per_scoop = 1.5
    total_money = 6
    total_scoops = (total_money / price_per_scoop) * 2
    result = total_scoops
    
    return result

print(solution())