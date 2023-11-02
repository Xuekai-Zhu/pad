def solution():
    """Gina is figuring out how much she'll have to spend on college this year. She's taking 14 credits that cost $450 each, and she has to pay $120 for each of her 5 textbooks plus a $200 facilities fee. How much will Gina spend in total?"""
    credits = 14
    cost_per_credit = 450
    textbooks = 5
    cost_per_textbook = 120
    facilities_fee = 200
    total_cost = (credits * cost_per_credit) + (textbooks * cost_per_textbook) + facilities_fee
    result = total_cost
    return result

print(solution())