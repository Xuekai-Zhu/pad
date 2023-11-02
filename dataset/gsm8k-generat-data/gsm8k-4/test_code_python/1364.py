def solution():
    """Gina is figuring out how much she'll have to spend on college this year. She's taking 14 credits that cost $450 each, and she has to pay $120 for each of her 5 textbooks plus a $200 facilities fee. How much will Gina spend in total?"""
    
    # Define the cost of each credit and the number of credits
    cost_per_credit = 450
    num_credits = 14

    # Define the cost of textbooks and the number of textbooks
    cost_per_textbook = 120
    num_textbooks = 5

    # Define the facilities fee
    facilities_fee = 200

    # Calculate the total cost of credits
    total_credit_cost = cost_per_credit * num_credits

    # Calculate the total cost of textbooks
    total_textbook_cost = cost_per_textbook * num_textbooks

    # Calculate the total cost of college
    total_college_cost = total_credit_cost + total_textbook_cost + facilities_fee

    # return the result
    result = total_college_cost
    return result

print(solution())