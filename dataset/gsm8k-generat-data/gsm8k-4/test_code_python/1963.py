def solution():
    """Christine makes money by commission rate. She gets a 12% commission on all items she sells. This month, she sold $24000 worth of items. Sixty percent of all her earning will be allocated to her personal needs and the rest will be saved. How much did she save this month?"""
    # Define the total amount of sales and the commission rate
    sales_total = 24000
    commission_rate = 0.12

    # Calculate the commission earned on the sales
    commission_earned = sales_total * commission_rate

    # Calculate the amount allocated to personal needs
    personal_needs = commission_earned * 0.6

    # Calculate the amount saved
    savings = commission_earned * 0.4

    result = savings
    return result

print(solution())