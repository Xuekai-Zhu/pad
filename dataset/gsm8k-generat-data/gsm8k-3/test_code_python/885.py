def solution():
    """Bobby needs to buy a new pair of fancy shoes.  He decides to go to a cobbler and get them handmade.
    The cobbler charges $250 to make the mold.  He then charges $75 an hour for 8 hours to make the shoes.
    The cobbler agrees to only charge 80% of the cost for work to make the shoes, since it is his first pair of shoes. How much did Bobby pay?"""
    
    # Define the charges by the cobbler
    MOLD_CHARGE = 250
    HOURLY_CHARGE = 75
    HOURS_WORKED = 8
    DISCOUNT = 0.8

    # Calculate the cost of making the shoes
    labor_cost = HOURLY_CHARGE * HOURS_WORKED
    total_cost = MOLD_CHARGE + labor_cost
    
    # Apply the discount
    discounted_cost = total_cost * DISCOUNT
    
    # Display the final cost Bobby paid
    result = discounted_cost
    return result

print(solution())