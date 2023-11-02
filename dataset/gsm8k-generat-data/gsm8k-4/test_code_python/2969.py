def solution():
    """Frank's laundry detergent is double concentrated and will wash 80 loads of laundry. His detergent is usually $25.00 a bottle but they're having a sale. If he buys 2 bottles, both bottles will drop to $20.00 a bottle. How much does he spend, in cents, per load of laundry, if he buys 2 bottles of detergent?"""
    # Define the original price and the sale price of the detergent
    ORIGINAL_PRICE = 25.00
    SALE_PRICE = 20.00

    # Define the number of bottles purchased and the number of loads of laundry per bottle
    NUM_BOTTLES = 2
    LOADS_PER_BOTTLE = 80

    # Calculate the total cost of purchasing the detergent
    if NUM_BOTTLES == 2:
        total_cost = SALE_PRICE * NUM_BOTTLES
    else:
        total_cost = ORIGINAL_PRICE * NUM_BOTTLES

    # Calculate the cost per load of laundry
    cost_per_load = total_cost / (NUM_BOTTLES * LOADS_PER_BOTTLE)
    cost_per_load_cents = cost_per_load * 100

    # return the result
    result = cost_per_load_cents
    return result

print(solution())