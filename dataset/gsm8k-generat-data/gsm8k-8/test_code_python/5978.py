def solution():
    # Calculate the total number of beads
    total_beads = 528

    # Divide by 3 to get the number of large beads
    large_beads = total_beads / 3

    # Use the given number of large beads to find the number of small beads
    small_beads = large_beads * 2

    # Calculate the number of bracelets that can be made with the given number of beads
    bracelets = large_beads / 12

    result = bracelets
    return result

print(solution())