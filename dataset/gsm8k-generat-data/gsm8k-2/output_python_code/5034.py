def solution():
    """An investment bank gives 10 percent interest at the end of every month. How much money in total will you have, including interest, at the end of 2 months if you invest $300?"""
    initial_investment = 300
    monthly_interest_rate = 0.1
    first_month_total = initial_investment + (initial_investment * monthly_interest_rate)
    second_month_total = first_month_total + (first_month_total * monthly_interest_rate)
    total_amount = round(second_month_total, 2)
    result = total_amount
    return result

print(solution())