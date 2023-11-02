def solution():
    num_credits = 14
    cost_per_credit = 450
    num_textbooks = 5
    cost_per_textbook = 120
    facilities_fee = 200

    # Calculate the total cost of credits
    credit_cost = num_credits * cost_per_credit

    # Calculate the total cost of textbooks
    textbook_cost = num_textbooks * cost_per_textbook

    # Calculate the total cost of all expenses
    total_cost = credit_cost + textbook_cost + facilities_fee
    result = total_cost
    return result

print(solution())