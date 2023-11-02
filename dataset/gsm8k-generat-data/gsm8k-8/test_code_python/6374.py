def solution():
    # Define the number of triple-flips Jen did
    jen_triples = 16

    # Calculate the number of flips Tyler did
    tyler_flips = jen_triples * 3 / 2

    # Calculate the number of double-flips Tyler did
    tyler_doubles = tyler_flips / 2
    result = tyler_doubles
    return result

print(solution())