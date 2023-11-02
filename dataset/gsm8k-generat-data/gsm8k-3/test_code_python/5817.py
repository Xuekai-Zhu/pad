def solution():
    """Jenny wants to sell some girl scout cookies and has the choice of two neighborhoods to visit.  Neighborhood A has 10 homes which each will buy 2 boxes of cookies.  Neighborhood B has 5 homes, each of which will buy 5 boxes of cookies.  Assuming each box of cookies costs $2, how much will Jenny make at the better choice of the two neighborhoods?"""
    # Define the number of boxes sold in each neighborhood
    NEIGH_A_BOXES = 2
    NEIGH_B_BOXES = 5

    # Define the price per box
    BOX_PRICE = 2

    # Calculate the total sales in each neighborhood
    neigh_a_sales = 10 * NEIGH_A_BOXES * BOX_PRICE
    neigh_b_sales = 5 * NEIGH_B_BOXES * BOX_PRICE

    # Determine which neighborhood has a higher total sales
    if neigh_a_sales > neigh_b_sales:
        result = neigh_a_sales
    else:
        result = neigh_b_sales

    return result

print(solution())