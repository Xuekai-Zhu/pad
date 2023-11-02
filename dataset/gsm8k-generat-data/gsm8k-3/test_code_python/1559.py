def solution():
    """Maci is planning for the new school year and goes to the store to buy pens. She needs ten blue pens and 15 red pens. If a blue pen costs ten cents each and a red pen costs twice as much as the blue pen, how much money does Maci pay for the pens?"""
    # Define the cost of a blue pen and the cost of a red pen (twice the cost of a blue pen)
    BLUE_PEN_COST = 0.1
    RED_PEN_COST = 2 * BLUE_PEN_COST

    # Calculate the total cost of the blue pens
    blue_pen_cost = 10 * BLUE_PEN_COST

    # Calculate the total cost of the red pens
    red_pen_cost = 15 * RED_PEN_COST

    # Calculate the total cost of all the pens
    total_cost = blue_pen_cost + red_pen_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())