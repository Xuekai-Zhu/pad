def solution():
    initial_balance = 500
    rice_price = 20
    num_rice_packets = 2
    wheat_flour_price = 25
    num_wheat_flour_packets = 3
    soda_price = 150

    # Subtract the cost of the rice packets
    initial_balance -= rice_price * num_rice_packets

    # Subtract the cost of the wheat flour packets
    initial_balance -= wheat_flour_price * num_wheat_flour_packets

    # Subtract the cost of the soda
    initial_balance -= soda_price

    result = initial_balance
    return result

print(solution())