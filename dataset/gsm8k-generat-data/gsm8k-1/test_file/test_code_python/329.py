def solution():
    """Robert wants to buy a bookshelf and a sofa and has received two offers. Furniture United's offer includes a $1,350 advance payment and 6 monthly installments of $350 each. Cozy Homes' offer includes a $1,100 advance payment and 9 monthly installments of $250 each. What is the cost difference between the two offers?"""
    fu_advance = 1350
    fu_monthly_payment = 350
    fu_total_cost = fu_advance + (fu_monthly_payment * 6)

    ch_advance = 1100
    ch_monthly_payment = 250
    ch_total_cost = ch_advance + (ch_monthly_payment * 9)

    cost_difference = fu_total_cost - ch_total_cost

    return cost_difference

print(solution())