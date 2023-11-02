def solution():
    """Liam wants to go to Paris, but first, he has to pay his bills. His trip costs $7,000, and his bills cost $3,500. Knowing that Liam has saved $500/month for 2 years, how much money will he have left after paying his bills? """
    # Calculate the total amount of money Liam has saved over 2 years
    total_savings = 500 * 12 * 2 # 500 dollars saved each month for 2 years

    # Calculate the total cost of Liam's bills plus his trip to Paris
    total_cost = 3500 + 7000

    # Calculate the remaining amount of money Liam will have after paying his bills
    remaining_money = total_savings - total_cost

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())