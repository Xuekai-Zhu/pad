def solution():
    """Jimmy bought 3 pens for school for $1 each, 4 notebooks for $3 each and 2 folders for $5 each. If he paid with a $50 bill, how much change will he get back?"""
    # Define the prices and quantities of the items
    pens_price = 1
    pens_quantity = 3
    notebooks_price = 3
    notebooks_quantity = 4
    folders_price = 5
    folders_quantity = 2

    # Calculate the total cost of the items
    total_cost = (pens_price * pens_quantity) + (notebooks_price * notebooks_quantity) + (folders_price * folders_quantity)

    # Calculate the amount of change
    change = 50 - total_cost

    # return the result
    result = change
    return result

print(solution())