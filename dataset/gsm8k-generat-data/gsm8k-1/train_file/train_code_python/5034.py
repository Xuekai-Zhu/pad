def solution():
    """An investment bank gives 10 percent interest at the end of every month. How much money in total will you have, including interest, at the end of 2 months if you invest $300?"""
    initial_investment = 300
    monthly_interest_rate = 0.10
    months = 2
    total_interest = initial_investment * monthly_interest_rate * months
    final_balance = initial_investment + total_interest
    result = final_balance
    return result

print(solution())