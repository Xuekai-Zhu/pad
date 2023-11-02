def solution():
    """Victor works at Clucks Delux, a restaurant specializing in chicken. An order of Chicken Pasta uses 2 pieces of chicken, an order of Barbecue Chicken uses 3 pieces of chicken, and a family-size Fried Chicken Dinner uses 8 pieces of chicken. Tonight, Victor has 2 Fried Chicken Dinner orders, 6 Chicken Pasta orders, and 3 Barbecue Chicken orders. How many pieces of chicken does he need for all the orders?"""
    # Define the number of pieces of chicken used for each type of order
    pasta_chicken = 2
    bbq_chicken = 3
    fried_chicken = 8

    # Define the number of each type of order
    pasta_orders = 6
    bbq_orders = 3
    fried_orders = 2

    # Calculate the total number of pieces of chicken needed for all the orders
    total_chicken = (pasta_chicken * pasta_orders) + (bbq_chicken * bbq_orders) + (fried_chicken * fried_orders)

    result = total_chicken
    return result

print(solution())