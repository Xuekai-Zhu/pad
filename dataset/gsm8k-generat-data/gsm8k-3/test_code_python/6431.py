def solution():
    """John decided to sell his PlayStation to buy a new computer.  The computer's cost was $700 and the accessories cost was $200.  The PlayStation was worth $400 but he sold it for 20% less than its value.  How much money came out of his pocket?"""
    # Define the cost of the computer and accessories
    COMPUTER_COST = 700
    ACCESSORIES_COST = 200

    # Define the value and discount of the PlayStation
    PLAYSTATION_VALUE = 400
    PLAYSTATION_DISCOUNT = 0.2

    # Calculate the money John received for selling the PlayStation
    playstation_sale_price = PLAYSTATION_VALUE - PLAYSTATION_VALUE * PLAYSTATION_DISCOUNT

    # Calculate the total cost of the computer setup
    total_cost = COMPUTER_COST + ACCESSORIES_COST - playstation_sale_price

    # Display the money John came out of pocket
    result = total_cost
    return result

print(solution())