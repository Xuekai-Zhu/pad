def solution():
    # Calculate the sales tax and tip amount
    sales_tax = 0.04 * 100  # 4% sales tax on $100
    tip = 0.06 * 100  # 6% tip on $100

    # Calculate the total amount paid by Greg
    total_paid = 100 + sales_tax + tip
    result = total_paid
    return result

print(solution())