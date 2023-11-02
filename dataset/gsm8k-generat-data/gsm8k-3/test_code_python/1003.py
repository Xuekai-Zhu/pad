def solution():
    """Cheryl is signing up for a golf tournament that costs 20% more than her monthly cell phone expenses to enter the tournament. If Cheryl spends $400 more on her monthly cell phone expenses than on the electricity bill, which costs $800, calculate the total amount she pays upon signing up for the golf tournament."""
    # Define the cost of the electricity bill
    electricity_bill = 800

    # Calculate Cheryl's monthly cell phone expenses
    cell_phone_expenses = electricity_bill + 400

    # Calculate the cost of the golf tournament
    tournament_cost = cell_phone_expenses * 1.2

    # Calculate the total amount Cheryl pays upon signing up for the golf tournament
    total_cost = tournament_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())