def solution():
    # Calculate Cheryl's monthly cell phone expenses
    electricity_bill = 800
    monthly_phone_expenses = electricity_bill + 400

    # Calculate the cost of entering the golf tournament
    tournament_cost = 1.2 * monthly_phone_expenses

    # Calculate the total amount Cheryl pays
    total_cost = monthly_phone_expenses + tournament_cost
    result = total_cost
    return result

print(solution())