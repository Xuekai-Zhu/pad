def solution():
    cost_of_lunch = 100
    sales_tax_rate = 0.04  # 4% sales tax
    tip_rate = 0.06  # 6% tip

    # Calculate the amount of sales tax
    sales_tax = cost_of_lunch * sales_tax_rate

    # Calculate the amount of tip
    tip = cost_of_lunch * tip_rate

    # Calculate the total amount paid by Greg
    total_paid = cost_of_lunch + sales_tax + tip
    result = total_paid
    return result

print(solution())