def solution():
    """Donny saves $15 on Monday, $28 on Tuesday and $13 on Wednesday. On Thursday he spends half of his total savings so far. How much did he spend?"""
    savings_monday = 15
    savings_tuesday = 28
    savings_wednesday = 13
    total_savings = savings_monday + savings_tuesday + savings_wednesday
    spending_thursday = total_savings / 2
    result = spending_thursday
    return result

print(solution())