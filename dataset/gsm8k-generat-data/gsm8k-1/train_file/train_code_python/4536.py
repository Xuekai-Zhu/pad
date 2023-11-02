def solution():
    """Miranda wants to buy a pair of heels she saw online. She saved money for 3 months. Her sister heard that she was sad and gave her $50 for her to buy the heels. If she paid $260 in total for the heels, how much money did she save per month?"""
    total_cost = 260
    sister_contribution = 50
    amount_saved = total_cost - sister_contribution
    num_months = 3
    savings_per_month = amount_saved / num_months
    result = savings_per_month
    return result

print(solution())