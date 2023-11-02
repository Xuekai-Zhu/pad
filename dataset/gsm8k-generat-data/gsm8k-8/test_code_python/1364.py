def solution():
    credit_cost = 450
    num_credits = 14
    textbook_cost = 120
    num_textbooks = 5
    facilities_fee = 200

    # Calculate the total cost of credits
    credit_total_cost = credit_cost * num_credits

    # Calculate the total cost of textbooks
    textbook_total_cost = textbook_cost * num_textbooks

    # Calculate the total cost of everything
    total_cost = credit_total_cost + textbook_total_cost + facilities_fee

    result = total_cost
    return result

print(solution())