def solution():
    """Jason waits on a customer whose check comes to $15.00. Jason's state applies a 20% tax to restaurant sales. If the customer gives Jason a $20 bill and tells him to keep the change, how much is Jason's tip?"""
    check_amount = 15
    tax_percent = 20
    tax_amount = check_amount * (tax_percent / 100)
    total_amount = check_amount + tax_amount
    tip_amount = 20 - total_amount
    result = tip_amount
    return result

print(solution())