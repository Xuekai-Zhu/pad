def solution():
    barry_amount = 10.00  # Barry has $10.00 worth of dimes
    dan_amount = barry_amount / 2  # Dan has half the amount of Barry
    dan_amount += 0.20  # Dan found 2 more dimes
    num_dimes = dan_amount / 0.10  # Each dime is worth $0.10

    result = num_dimes
    return result

print(solution())