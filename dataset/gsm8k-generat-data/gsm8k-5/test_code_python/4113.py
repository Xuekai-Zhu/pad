def solution():
    # Calculate how much fabric Nicholas bought
    fabric_nicholas = 6 * 700

    # Calculate how much money Nicholas paid for the fabric
    price_nicholas = fabric_nicholas * 40

    # Calculate how much money Kenneth paid for the fabric
    price_kenneth = 700 * 40

    # Calculate the difference in the amounts paid by Nicholas and Kenneth
    difference = price_nicholas - price_kenneth
    result = difference
    return result

print(solution())