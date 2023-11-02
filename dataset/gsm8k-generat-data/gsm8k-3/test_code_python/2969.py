def solution():
    """Frank's laundry detergent is double concentrated and will wash 80 loads of laundry.  His detergent is usually $25.00 a bottle but they're having a sale.  If he buys 2 bottles, both bottles will drop to $20.00 a bottle.  How much does he spend, in cents, per load of laundry, if he buys 2 bottles of detergent?"""
    # Define the regular and sale prices of the detergent
    REGULAR_PRICE = 2500
    SALE_PRICE = 2000

    # Define the number of loads of laundry that the detergent will wash
    LOADS_PER_BOTTLE = 80

    # Calculate the cost per load of laundry for one bottle at regular price
    cost_per_load_regular = REGULAR_PRICE / LOADS_PER_BOTTLE

    # Calculate the cost per load of laundry for one bottle on sale
    cost_per_load_sale = SALE_PRICE / LOADS_PER_BOTTLE

    # Calculate the cost per load of laundry for two bottles on sale
    total_cost = 2 * SALE_PRICE
    total_loads = 2 * LOADS_PER_BOTTLE
    cost_per_load = total_cost / total_loads

    # Display the cost per load of laundry
    result = int(cost_per_load)
    return result

print(solution())