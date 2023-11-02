def solution():
    """Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?"""
    total_cost = 23
    base_price = 3
    cost_per_mile = 4
    distance = (total_cost - base_price) / cost_per_mile
    result = distance
    return result

print(solution())