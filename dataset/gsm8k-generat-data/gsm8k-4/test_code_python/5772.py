def solution():
    """Will's mom gave him $74 to go shopping. He bought a sweater for $9, a T-shirt for $11 and a pair of shoes for $30. He then returned his shoes for a 90% refund. How much money does Will have left?"""
    # Define the initial amount of money given to Will
    initial_money = 74

    # Define the prices of the sweater, T-shirt, and shoes
    sweater_price = 9
    tshirt_price = 11
    shoes_price = 30

    # Calculate the total cost of the items purchased
    total_cost = sweater_price + tshirt_price + shoes_price

    # Calculate the amount refunded for the shoes
    shoes_refund = shoes_price * 0.9

    # Calculate the final amount spent and the amount of money left
    final_spent = total_cost - shoes_price + shoes_refund
    money_left = initial_money - final_spent

    # return the result
    result = money_left
    return result

print(solution())