def solution():
    """Emily just purchased 2 pairs of curtains for $30.00 each and 9 wall prints at $15.00 each. The store also offers an installation service. For $50.00 they will come to your house and professionally hang your curtains and prints. If Emily agrees to this service, how much will her entire order cost?"""
    curtain_price = 30
    print_price = 15
    installation_price = 50
    total_price = (2 * curtain_price) + (9 * print_price) + installation_price
    result = total_price
    return result

print(solution())