def solution():
    """Mike and John dined at the Taco Palace restaurant.  They each ordered the Taco Grande Plate as their main meal, but Mike also ordered a side salad for $2, a plate of cheesy fries for $4, and a diet cola for $2.  As a result, Mike's lunch bill was twice as large as John's bill.  What was the combined total cost, in dollars, of Mike and John's lunch?"""
    # Define the cost of the Taco Grande Plate
    TACO_GRANDE_PRICE = 10

    # Define the cost of Mike's additional items
    SIDE_SALAD_PRICE = 2
    CHEESY_FRIES_PRICE = 4
    DIET_COLA_PRICE = 2

    # Calculate the total cost of John's lunch
    john_cost = TACO_GRANDE_PRICE

    # Calculate the total cost of Mike's lunch
    mike_cost = TACO_GRANDE_PRICE + SIDE_SALAD_PRICE + CHEESY_FRIES_PRICE + DIET_COLA_PRICE

    # Calculate the combined total cost of Mike and John's lunch
    total_cost = john_cost + mike_cost

    # Display the combined total cost
    result = total_cost
    return result

print(solution())