def solution():
    weekly_income = 500  # Alex gets paid $500 a week
    tax = 0.1 * weekly_income  # 10% of his weekly income is deducted as tax
    net_income = weekly_income - tax  # Calculate the net income after tax

    water_bill = 55  # Alex pays a weekly water bill of $55
    tithe = 0.1 * net_income  # 10% of his net income is given away as a tithe

    # Calculate the total amount of money Alex has left
    total_left = net_income - water_bill - tithe
    result = total_left
    return result

print(solution())