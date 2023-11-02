def solution():
    """Frank goes to the store to buy some food. He buys 5 chocolate bars and 2 bags of chips. He hands the cashier $20 and gets $4 back as change. If the chocolate bars each cost $2, how much did each bag of chips cost?"""
    # Define the number of chocolate bars and bags of chips purchased, and the total amount paid
    chocolate_bars = 5
    chips_bags = 2
    total_paid = 20

    # Calculate the total cost of the chocolate bars
    chocolate_cost = chocolate_bars * 2

    # Calculate the amount paid for the chips and the total cost of the purchase
    chips_cost = total_paid - chocolate_cost - 4
    total_cost = chocolate_cost + chips_cost

    # Calculate the cost per bag of chips
    chip_price = chips_cost / chips_bags

    result = chip_price
    return result

print(solution())