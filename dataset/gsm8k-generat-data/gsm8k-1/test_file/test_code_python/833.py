def solution():
    """Erika is saving for a new laptop. The laptop she wants costs $600. The sales assistant told her that if she traded in her old laptop, the price of the new one would be reduced by $200. She already has some savings in her purse, and has also been paid $150 this week for her part-time job. Her mom agrees to give her $80 to help her. If Erika now only needs an extra $50 to buy the laptop, how much money does she have in her purse?"""
    laptop_cost = 600
    trade_in_discount = 200
    total_discount = laptop_cost - trade_in_discount
    purse_savings = total_discount - 50 - 150 - 80
    result = purse_savings
    return result

print(solution())