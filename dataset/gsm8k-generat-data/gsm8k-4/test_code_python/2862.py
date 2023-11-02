def solution():
    """Emily just purchased 2 pairs of curtains for $30.00 each and 9 wall prints at $15.00 each. The store also offers an installation service. For $50.00 they will come to your house and professionally hang your curtains and prints. If Emily agrees to this service, how much will her entire order cost?"""
    # Calculate the cost of the curtains
    curtain_cost = 2 * 30

    # Calculate the cost of the wall prints
    print_cost = 9 * 15

    # Calculate the cost of the installation service
    install_cost = 50

    # Calculate the total cost of Emily's order
    total_cost = curtain_cost + print_cost + install_cost

    # return the result
    result = total_cost
    return result

print(solution())