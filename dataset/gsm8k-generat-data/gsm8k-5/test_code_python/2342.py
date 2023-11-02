def solution():
    monthly_rate = 50  # Monthly internet rate is $50
    discount_rate = 0.05  # 5% discount if customer pays before the 25th of the month
    discounted_rate = monthly_rate - (monthly_rate * discount_rate)  # Calculate the discounted rate

    # Calculate the total amount paid for 4 months, including the discount
    total_amount_paid = (discounted_rate * 4 * 25) + (monthly_rate * 4 * (31-25))

    result = total_amount_paid
    return result

print(solution())