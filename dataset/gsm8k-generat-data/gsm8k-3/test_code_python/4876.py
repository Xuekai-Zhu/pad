def solution():
    """MegaCorp got caught leaking carcinogens into the water supply and is being fined 1% of its annual profits. Every day MegaCorp earns $3,000,000 from mining and $5,000,000 from oil refining. Its monthly expenses are $30,000,000. How much is MegaCorp's fine in dollars?"""
    # Calculate MegaCorp's daily revenue
    daily_revenue = 3000000 + 5000000

    # Calculate MegaCorp's monthly revenue
    monthly_revenue = daily_revenue * 30

    # Calculate MegaCorp's annual revenue
    annual_revenue = monthly_revenue * 12

    # Calculate MegaCorp's annual profit after expenses
    annual_profit = annual_revenue - (30000000 * 12)

    # Calculate MegaCorp's fine
    fine = annual_profit * 0.01

    # Display the fine
    result = fine
    return result

print(solution())