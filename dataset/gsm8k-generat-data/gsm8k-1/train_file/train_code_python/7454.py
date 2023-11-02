def solution():
    """Jim decides to open up a bike shop. The most common repair he does is fixing bike tires. He charges $20 for this and it cost him $5 in parts. In one month Jim does 300 of these repairs. He also does 2 more complex repairs for $300 each and cost $50 in parts. He also sells $2000 profit worth of things from his retail shop. If rent and other fixed expense for the shop is $4000 a month how much profit did the shop make?"""
    tire_repair_price = 20
    tire_repair_cost = 5
    tire_repairs_per_month = 300
    complex_repair_price = 300
    complex_repair_cost = 50
    complex_repairs_per_month = 2
    retail_profit = 2000
    fixed_expenses = 4000

    total_profit = (tire_repair_price - tire_repair_cost) * tire_repairs_per_month \
                   + (complex_repair_price - complex_repair_cost) * complex_repairs_per_month \
                   + retail_profit \
                   - fixed_expenses

    result = total_profit
    return result

print(solution())