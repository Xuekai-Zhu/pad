def solution():
    """Tim gets a manicure and tips the beautician 30%. If the manicure cost $30 how much did he pay in total?"""
    manicure_cost = 30
    tip_percent = 30
    tip_amount = manicure_cost * (tip_percent / 100)
    total_cost = manicure_cost + tip_amount
    result = total_cost
    return result

print(solution())