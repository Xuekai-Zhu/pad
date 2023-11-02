def solution():
    """Jason waits on a customer whose check comes to $15.00. Jason's state applies a 20% tax to restaurant sales. If the customer gives Jason a $20 bill and tells him to keep the change, how much is Jason's tip?"""
    check_amount = 15.00
    tax_rate = 0.20
    tax_amount = check_amount * tax_rate
    total_amount = check_amount + tax_amount
    tip = 20.00 - total_amount
    result = tip
    return result

print(solution())