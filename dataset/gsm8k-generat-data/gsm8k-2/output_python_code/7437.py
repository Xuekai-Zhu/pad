def solution():
    """Logan makes $65,000 a year. He spends $20,000 on rent every year, $5000 on groceries every year, and $8000 on gas every year. 
    If he wants to have at least $42,000 left, how much more money must he make each year?"""
    income = 65000
    expenses = 20000 + 5000 + 8000
    savings_goal = 42000
    additional_income_needed = (expenses + savings_goal) - income
    result = additional_income_needed
    return result

print(solution())