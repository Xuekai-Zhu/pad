def solution():
    # Calculate the total cost of buying the television on credit
    total_cost_on_credit = 120 + (30 * 12)  # $120 as down payment, $30 per month for 12 months

    # Calculate the amount saved by paying cash
    amount_saved = total_cost_on_credit - 400

    result = amount_saved
    return result

print(solution())