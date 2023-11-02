def solution():
    """Gina is figuring out how much she'll have to spend on college this year. She's taking 14 credits that cost $450 each, and she has to pay $120 for each of her 5 textbooks plus a $200 facilities fee. How much will Gina spend in total?"""
    # Define the cost of each credit and the number of credits
    CREDIT_COST = 450
    NUM_CREDITS = 14

    # Define the cost of each textbook and the number of textbooks
    TEXTBOOK_COST = 120
    NUM_TEXTBOOKS = 5

    # Define the facilities fee
    FACILITIES_FEE = 200

    # Calculate the total cost of credits
    credit_cost_total = CREDIT_COST * NUM_CREDITS

    # Calculate the total cost of textbooks
    textbook_cost_total = TEXTBOOK_COST * NUM_TEXTBOOKS

    # Calculate the total cost
    total_cost = credit_cost_total + textbook_cost_total + FACILITIES_FEE

    # Display the total cost
    result = total_cost
    return result

print(solution())