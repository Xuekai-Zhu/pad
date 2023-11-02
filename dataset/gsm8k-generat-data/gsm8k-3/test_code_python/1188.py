def solution():
    """Preston has a sandwich shop. He charges $5 for each sandwich. He also charges $20 for a delivery fee. Abra Company orders 18 sandwiches from Preston and also tips him 10%. How much total, in dollars, did Preston receive?"""
    # Define the sandwich price and delivery fee
    SANDWICH_PRICE = 5
    DELIVERY_FEE = 20

    # Calculate the cost of the sandwiches
    sandwich_cost = SANDWICH_PRICE * 18

    # Calculate the tip amount
    tip_amount = sandwich_cost * 0.1

    # Calculate the total amount received
    total_amount = sandwich_cost + tip_amount + DELIVERY_FEE

    # Display the total amount received
    result = total_amount
    return result

print(solution())