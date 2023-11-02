def solution():
    """Frank goes to the store to buy some food. He buys 5 chocolate bars and 2 bags of chips. He hands the cashier $20 and gets $4 back as change. If the chocolate bars each cost $2, how much did each bag of chips cost?"""
    num_chocolate = 5
    chocolate_price = 2
    total_chocolate_price = num_chocolate * chocolate_price
    total_paid = 20
    change = 4
    total_food_price = total_paid - change
    total_chips_price = total_food_price - total_chocolate_price
    num_chips = 2
    chips_price = total_chips_price / num_chips
    result = chips_price
    return result

print(solution())