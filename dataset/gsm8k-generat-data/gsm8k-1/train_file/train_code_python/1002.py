def solution():
    """Cheryl is signing up for a golf tournament that costs 20% more than her monthly cell phone expenses to enter the tournament. If Cheryl spends $400 more on her monthly cell phone expenses than on the electricity bill, which costs $800, calculate the total amount she pays upon signing up for the golf tournament."""
    electricity_bill = 800
    cell_phone_expenses = electricity_bill + 400
    tournament_cost = cell_phone_expenses * 1.2
    total_cost = tournament_cost + cell_phone_expenses + electricity_bill
    result = total_cost
    return result

print(solution())