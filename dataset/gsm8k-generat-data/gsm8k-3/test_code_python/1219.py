def solution():
    """Victor works at Clucks Delux, a restaurant specializing in chicken. An order of Chicken Pasta uses 2 pieces of chicken, an order of Barbecue Chicken uses 3 pieces of chicken, and a family-size Fried Chicken Dinner uses 8 pieces of chicken. Tonight, Victor has 2 Fried Chicken Dinner orders, 6 Chicken Pasta orders, and 3 Barbecue Chicken orders. How many pieces of chicken does he need for all the orders?"""
    # Define the number of pieces of chicken needed for each type of order
    PASTA_CHICKEN = 2
    BBQ_CHICKEN = 3
    FRIED_CHICKEN = 8

    # Define the number of orders for each type of chicken dish
    pasta_orders = 6
    bbq_orders = 3
    fried_orders = 2

    # Calculate the total number of pieces of chicken needed
    total_chicken = (PASTA_CHICKEN * pasta_orders) + (BBQ_CHICKEN * bbq_orders) + (FRIED_CHICKEN * fried_orders)

    # Display the total number of pieces of chicken needed
    result = total_chicken
    return result

print(solution())