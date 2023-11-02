def solution():
    # Let x be the number of tent stakes Rebecca bought
    x = 0

    # Calculate the number of packets of drink mix Rebecca bought (3 times the number of tent stakes)
    drink_packets = 3 * x

    # Calculate the number of bottles of water Rebecca bought (2 more than the number of tent stakes)
    water_bottles = x + 2

    # Calculate the total number of items Rebecca bought (sum of tent stakes, drink packets, and water bottles)
    total_items = x + drink_packets + water_bottles

    # Since the total number of items is given as 22, we can solve for x: x + 3x + (x+2) = 22
    x = (22 - 2) / 5

    result = x
    return result

print(solution())