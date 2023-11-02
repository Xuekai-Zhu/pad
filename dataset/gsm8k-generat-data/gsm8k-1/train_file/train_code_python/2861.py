def solution():
    """Emily just purchased 2 pairs of curtains for $30.00 each and 9 wall prints at $15.00 each. The store also offers an installation service. For $50.00 they will come to your house and professionally hang your curtains and prints. If Emily agrees to this service, how much will her entire order cost?"""
    curtain_price = 30
    print_price = 15
    number_of_curtains = 2
    number_of_prints = 9
    installation_service_cost = 50
    total_cost = (curtain_price * number_of_curtains) + (print_price * number_of_prints) + installation_service_cost
    result = total_cost
    return result

print(solution())