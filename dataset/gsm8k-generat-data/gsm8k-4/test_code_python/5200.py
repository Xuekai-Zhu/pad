def solution():
    """Bryan bought 5 t-shirts and 4 pairs of pants for $1500. If a t-shirt costs $100, how much does each pair of pants cost?"""
    # Define the cost of a t-shirt
    tshirt_cost = 100

    # Define the number of t-shirts and pants
    tshirt_count = 5
    pant_count = 4

    # Calculate the total cost of t-shirts
    tshirt_total_cost = tshirt_count * tshirt_cost

    # Calculate the cost of pants
    pant_cost = (1500 - tshirt_total_cost)/pant_count

    # return the result
    result = pant_cost
    return result

print(solution())