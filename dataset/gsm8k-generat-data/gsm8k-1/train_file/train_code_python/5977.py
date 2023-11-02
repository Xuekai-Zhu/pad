def solution():
    """Caitlin makes bracelets to sell at the farmer’s market every weekend. Each bracelet takes twice as many small beads as it does large beads. If each bracelet uses 12 large beads, and Caitlin has 528 beads with equal amounts of large and small beads, how many bracelets can she make for this weekend?"""
    large_beads_per_bracelet = 12
    total_beads = 528
    small_beads_per_bracelet = 2 * large_beads_per_bracelet
    total_large_beads = total_beads / 2
    total_bracelets = total_large_beads / large_beads_per_bracelet
    result = total_bracelets
    return result

print(solution())