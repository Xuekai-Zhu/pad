def solution():
    # Let x be the number of earrings that Rachel has
    x = 1
    # Calculate the number of earrings Monica has
    monica_earrings = 2 * x
    # Calculate the number of earrings Bella has
    bella_earrings = 0.25 * monica_earrings
    # Calculate the total number of earrings
    total_earrings = x + monica_earrings + bella_earrings
    result = total_earrings
    return result

print(solution())