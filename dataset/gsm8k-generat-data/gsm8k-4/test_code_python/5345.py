def solution():
    """Lee wants to propose marriage to Sierra. He wants to follow the adage that you should spend two months' salary on the ring. He earns $60,000 per year in salary and can save $1000 per month. How long will it take before he can propose to Sierra?"""
    # Define the target amount to be spent on the ring
    target_amount = 2 * 60000 / 12

    # Define Lee's monthly savings
    monthly_savings = 1000

    # Calculate the number of months it will take to save enough for the ring
    months = target_amount / monthly_savings

    # Display the result
    result = round(months)
    return result

print(solution())