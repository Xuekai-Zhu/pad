def solution():
    """John's hair grows 1.5 inches every month. Every time it gets to 9 inches long he cuts it down to 6 inches. A haircut costs $45 and he gives a 20% tip. How much does he spend on haircuts a year?"""
    growth_per_month = 1.5
    cut_length = 9
    cut_cost = 45
    tip_percent = 20

    # Calculate how many haircuts John needs per year
    months_per_year = 12
    months_between_cuts = (cut_length - 6) / growth_per_month
    haircuts_per_year = months_per_year / months_between_cuts

    # Calculate the total cost of haircuts per year
    tip_amount = cut_cost * (tip_percent / 100)
    total_cost_per_haircut = cut_cost + tip_amount
    total_cost_per_year = total_cost_per_haircut * haircuts_per_year

    result = total_cost_per_year
    return result

print(solution())