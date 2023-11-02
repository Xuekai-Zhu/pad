def solution():
    """It costs $.10 to print one page. Jenny wants to print 7 copies of her 25-page essay. She also wants to buy 7 pens that each cost $1.50. If she pays the store with 2 twenty dollar bills, how much money should she get in change?"""
    # Define the cost of printing the essay and the number of copies
    PRINTING_COST = 0.1
    COPIES = 7
    PAGES = 25

    # Calculate the total cost of printing the essay
    printing_total = PRINTING_COST * COPIES * PAGES

    # Define the cost of the pens and the number of pens
    PEN_COST = 1.5
    NUM_PENS = 7

    # Calculate the total cost of the pens
    pens_total = PEN_COST * NUM_PENS

    # Define the amount Jenny pays
    payment = 40

    # Calculate the total cost of the purchase and the change
    total_cost = printing_total + pens_total
    change = payment - total_cost

    # Return the amount of change
    result = change
    return result

print(solution())