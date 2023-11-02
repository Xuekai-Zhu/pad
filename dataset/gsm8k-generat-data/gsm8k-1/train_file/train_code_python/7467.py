def solution():
    """Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?"""
    base_price = 3
    total_price = 23
    price_per_mile = 4
    miles_traveled = (total_price - base_price) / price_per_mile
    result = miles_traveled
    return result

print(solution())