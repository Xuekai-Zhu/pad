def solution():
    """Bobby needs to buy a new pair of fancy shoes. He decides to go to a cobbler and get them handmade. The cobbler charges $250 to make the mold. He then charges $75 an hour for 8 hours to make the shoes. The cobbler agrees to only charge 80% of the cost for work to make the shoes since it is his first pair of shoes. How much did Bobby pay?"""
    # Define the cost for making the mold
    mold_cost = 250

    # Define the cost per hour for making the shoes and the time it takes to make them
    hourly_cost = 75
    time = 8

    # Calculate the total cost for making the shoes
    total_cost = mold_cost + (hourly_cost * time)

    # Calculate the cost with the discount
    discounted_cost = total_cost * 0.8

    # Return the final cost
    result = discounted_cost
    return result

print(solution())