def solution():
    """John decided to sell his PlayStation to buy a new computer. The computer's cost was $700 and the accessories cost was $200. The PlayStation was worth $400 but he sold it for 20% less than its value. How much money came out of his pocket?"""
    # Define the cost of the computer and accessories
    computer_cost = 700
    accessories_cost = 200

    # Define the original value of the PlayStation and the percentage it was sold for
    ps4_original_value = 400
    ps4_discount_percentage = 20

    # Calculate the amount John received for the PlayStation after the discount
    ps4_discount = ps4_original_value * (ps4_discount_percentage / 100)
    ps4_sale_price = ps4_original_value - ps4_discount

    # Calculate the total amount of money John spent
    total_spent = computer_cost + accessories_cost - ps4_sale_price

    # The result is the total amount John spent
    result = total_spent
    return result

print(solution())