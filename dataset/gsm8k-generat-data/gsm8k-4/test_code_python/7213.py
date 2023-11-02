def solution():
    """Mike and John dined at the Taco Palace restaurant.  They each ordered the Taco Grande Plate as their main meal, but Mike also ordered a side salad for $2, a plate of cheesy fries for $4, and a diet cola for $2.  As a result, Mike's lunch bill was twice as large as John's bill.  What was the combined total cost, in dollars, of Mike and John's lunch?"""
    # Define the cost of the Taco Grande Plate
    taco_grande_price = 10

    # Calculate the cost of Mike's lunch
    mikes_lunch = taco_grande_price + 2 + 4 + 2

    # Calculate the cost of John's lunch (half the cost of Mike's lunch)
    johns_lunch = mikes_lunch / 2

    # Calculate the combined total cost of Mike and John's lunch
    total_cost = mikes_lunch + johns_lunch

    # Return the result
    result = total_cost
    return result

print(solution())