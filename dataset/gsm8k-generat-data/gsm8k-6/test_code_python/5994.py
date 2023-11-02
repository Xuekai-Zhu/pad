def solution():
    # Set up the equations for the number of gemstones on each cat's collar
    # Binkie has 4 times as many as Frankie
    # Spaatz has 2 less than half as many as Frankie
    # If Spaatz has 1 gemstone, we can solve for Frankie's number of gemstones
    frankie_gemstones = (1 + 2) * 2  # Spaatz has 2 less than half as many as Frankie
    binkie_gemstones = 4 * frankie_gemstones  # Binkie has 4 times as many as Frankie
    result = binkie_gemstones
    return result

print(solution())