def solution():
    electricity_bill = 800  # Cheryl's electricity bill costs $800
    cell_phone_expenses = electricity_bill + 400  # Cheryl spends $400 more on her cell phone expenses than on the electricity bill
    tournament_cost = 1.2 * cell_phone_expenses  # The golf tournament costs 20% more than Cheryl's monthly cell phone expenses

    # Calculate the total amount Cheryl pays upon signing up for the golf tournament
    total_amount = cell_phone_expenses + tournament_cost
    result = total_amount
    return result

print(solution())