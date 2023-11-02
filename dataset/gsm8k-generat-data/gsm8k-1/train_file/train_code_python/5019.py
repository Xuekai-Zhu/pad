def solution():
    """Alice was able to sell $2500 worth of gadgets. For this month, she expects to receive her monthly basic salary of $240 and a 2% commission from these sales. How much is she going to save this month if she usually saves 10% of her total earnings?"""
    gadget_sales = 2500
    commission_rate = 0.02
    commission_earned = gadget_sales * commission_rate
    basic_salary = 240
    total_income = basic_salary + commission_earned + gadget_sales
    savings_rate = 0.1
    savings_amount = total_income * savings_rate
    result = savings_amount
    return result

print(solution())