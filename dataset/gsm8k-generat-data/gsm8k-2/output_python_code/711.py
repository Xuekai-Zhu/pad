def solution():
    """Jimmy bought 3 pens for school for $1 each, 4 notebooks for $3 each and 2 folders for $5 each. If he paid with a $50 bill, how much change will he get back?"""
    total_cost = (3 * 1) + (4 * 3) + (2 * 5)  # cost of all items
    change = 50 - total_cost  # subtract total cost from $50 bill to get change
    result = change
    return result

print(solution())