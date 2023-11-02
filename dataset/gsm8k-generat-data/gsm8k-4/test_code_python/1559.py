def solution():
    """Maci is planning for the new school year and goes to the store to buy pens. She needs ten blue pens and 15 red pens. If a blue pen costs ten cents each and a red pen costs twice as much as the blue pen, how much money does Maci pay for the pens?"""
    # Define the number of blue pens and red pens needed
    blue_pens = 10
    red_pens = 15

    # Define the price of a blue pen and the price of a red pen
    blue_price = 0.10
    red_price = blue_price * 2

    # Calculate the total cost of the blue pens
    blue_cost = blue_pens * blue_price

    # Calculate the total cost of the red pens
    red_cost = red_pens * red_price

    # Calculate the total cost of all the pens
    total_cost = blue_cost + red_cost

    # return the result
    result = total_cost
    return result

print(solution())