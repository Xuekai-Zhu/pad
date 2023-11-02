def solution():
    """Caitlin makes bracelets to sell at the farmer's market every weekend. Each bracelet takes twice as many small beads as it does large beads. If each bracelet uses 12 large beads, and Caitlin has 528 beads with equal amounts of large and small beads, how many bracelets can she make for this weekend?"""
    # Calculate the total number of large beads
    large_beads_total = 528 / 2
    large_beads_per_bracelet = 12

    # Calculate the total number of bracelets she can make
    bracelets = large_beads_total / large_beads_per_bracelet

    result = int(bracelets)
    return result

print(solution())