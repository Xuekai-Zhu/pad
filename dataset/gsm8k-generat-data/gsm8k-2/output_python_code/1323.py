def solution():
    """After working out for 3 hours, three friends go out for lunch. Adam spends two-thirds as much money on lunch as Rick. Rick and Jose eat lunch of the same price. If Jose ate lunch worth $45, what is the cost of lunch for all three?"""
    jose_price = 45
    rick_price = jose_price
    adam_price = (2/3) * rick_price
    total_price = jose_price + rick_price + adam_price
    result = total_price
    return result

print(solution())