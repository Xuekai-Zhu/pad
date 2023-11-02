def solution():
    """The movie theater sells matinee tickets for $5, evening tickets for $12, and 3D tickets for $20. If they sell 200 matinee tickets, 300 evening tickets and 100 3D tickets, how much money do they make in total?"""
    # Define the prices and quantities of tickets
    MATINEE_PRICE = 5
    EVENING_PRICE = 12
    THREED_PRICE = 20
    MATINEE_QUANTITY = 200
    EVENING_QUANTITY = 300
    THREED_QUANTITY = 100

    # Calculate the total money made from each type of ticket and sum them up
    matinee_money = MATINEE_PRICE * MATINEE_QUANTITY
    evening_money = EVENING_PRICE * EVENING_QUANTITY
    threed_money = THREED_PRICE * THREED_QUANTITY

    total_money = matinee_money + evening_money + threed_money

    # Return the result
    result = total_money
    return result

print(solution())