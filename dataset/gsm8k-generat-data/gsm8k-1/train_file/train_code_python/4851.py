def solution():
    """A newspaper subscription costs $10/month. If you purchase an annual subscription you obtain a 20% discount on your total bill. How much do you end up paying if you go with the annual subscription?"""
    monthly_cost = 10
    discount_percentage = 20
    num_months = 12

    total_cost = monthly_cost * num_months
    discount_amount = total_cost * (discount_percentage / 100)
    discounted_total = total_cost - discount_amount

    result = discounted_total
    return result

print(solution())