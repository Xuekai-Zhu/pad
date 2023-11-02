def solution():
    """Jimmy bought 3 pens for school for $1 each, 4 notebooks for $3 each and 2 folders for $5 each. If he paid with a $50 bill, how much change will he get back?"""
    # Define the prices of each item
    PEN_PRICE = 1
    NOTEBOOK_PRICE = 3
    FOLDER_PRICE = 5

    # Define the number of each item purchased
    num_pens = 3
    num_notebooks = 4
    num_folders = 2

    # Calculate the total cost of the items
    total_cost = (num_pens * PEN_PRICE) + (num_notebooks * NOTEBOOK_PRICE) + (num_folders * FOLDER_PRICE)

    # Calculate the change Jimmy will receive
    change = 50 - total_cost

    # Display the change
    result = change
    return result

print(solution())