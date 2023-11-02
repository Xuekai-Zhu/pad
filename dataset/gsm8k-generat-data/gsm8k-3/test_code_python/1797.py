def solution():
    """John buys 3 t-shirts that cost $20 each.  He also buys $50 in pants.  How much does he spend?"""
    # Define the cost of each t-shirt and the cost of pants
    TSHIRT_PRICE = 20
    PANTS_PRICE = 50

    # Define the number of t-shirts purchased
    tshirt_count = 3

    # Calculate the total cost of the t-shirts and pants
    tshirt_cost = TSHIRT_PRICE * tshirt_count
    pants_cost = PANTS_PRICE
    total_cost = tshirt_cost + pants_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())