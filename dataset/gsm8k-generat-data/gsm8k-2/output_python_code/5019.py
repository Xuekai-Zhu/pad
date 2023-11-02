def solution():
    """Alice was able to sell $2500 worth of gadgets. For this month, she expects to receive her monthly basic salary of $240 and a 2% commission from these sales. How much is she going to save this month if she usually saves 10% of her total earnings?"""
    sales_amount = 2500
    commission_rate = 0.02
    commission_earnings = sales_amount * commission_rate
    basic_salary = 240
    total_earnings = commission_earnings + basic_salary
    savings_rate = 0.1
    total_savings = total_earnings * savings_rate
    result = total_savings
    return result

print(solution())