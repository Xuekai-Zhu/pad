def solution():
    credit_cost = 450  # Each credit costs $450
    num_credits = 14  # Gina is taking 14 credits
    textbook_cost = 120  # Each textbook costs $120
    num_textbooks = 5  # Gina needs 5 textbooks
    facilities_fee = 200  # There is a $200 facilities fee

    # Calculate the total cost of credits
    credit_total = credit_cost * num_credits

    # Calculate the total cost of textbooks
    textbook_total = textbook_cost * num_textbooks

    # Calculate the total cost of college
    total_cost = credit_total + textbook_total + facilities_fee
    result = total_cost
    return result

print(solution())