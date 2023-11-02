def solution():
    """Gina is figuring out how much she'll have to spend on college this year. She's taking 14 credits that cost $450 each, and she has to pay $120 for each of her 5 textbooks plus a $200 facilities fee. How much will Gina spend in total?"""
    credit_cost = 450
    num_credits = 14
    textbook_cost = 120
    num_textbooks = 5
    facilities_fee = 200
    total_cost = (credit_cost * num_credits) + (textbook_cost * num_textbooks) + facilities_fee
    result = total_cost
    return result

print(solution())