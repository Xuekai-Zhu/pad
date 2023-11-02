def solution():
    """Liam wants to go to Paris, but first, he has to pay his bills. His trip costs $7,000, and his bills cost $3,500. Knowing that Liam has saved $500/month for 2 years, how much money will he have left after paying his bills?"""
    # Define the cost of Liam's trip and his bills
    trip_cost = 7000
    bills_cost = 3500

    # Define Liam's monthly savings amount and the number of months he saved for
    monthly_savings = 500
    num_months = 24

    # Calculate the total amount Liam saved
    total_savings = monthly_savings * num_months

    # Calculate the amount of money Liam will have left after paying his bills and trip cost
    remaining_money = total_savings - bills_cost - trip_cost

    result = remaining_money
    return result

print(solution())