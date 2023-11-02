def solution():
    """Jane is trying to decide whether to buy a house or a trailer. A house costs $480,000 and a trailer costs $120,000. Each loan will be paid in monthly installments over 20 years. How much more is the monthly payment on the house compared to the trailer?"""
    house_cost = 480000
    trailer_cost = 120000
    years = 20
    months = years * 12
    house_monthly_payment = house_cost / months
    trailer_monthly_payment = trailer_cost / months
    monthly_difference = house_monthly_payment - trailer_monthly_payment
    result = monthly_difference
    return result

print(solution())