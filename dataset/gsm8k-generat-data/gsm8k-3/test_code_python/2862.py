def solution():
    """Emily just purchased 2 pairs of curtains for $30.00 each and 9 wall prints at $15.00 each.  The store also offers an installation service.  For $50.00 they will come to your house and professionally hang your curtains and prints.  If Emily agrees to this service, how much will her entire order cost?"""
    # Define the prices of the curtains and wall prints
    CURTAIN_PRICE = 30
    PRINT_PRICE = 15

    # Define the quantities of curtains and wall prints purchased
    curtain_qty = 2
    print_qty = 9

    # Calculate the total cost of the curtains
    curtain_cost = curtain_qty * CURTAIN_PRICE

    # Calculate the total cost of the wall prints
    print_cost = print_qty * PRINT_PRICE

    # Calculate the total cost of the installation service
    installation_cost = 50

    # Calculate the total cost of Emily's order
    total_cost = curtain_cost + print_cost + installation_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())