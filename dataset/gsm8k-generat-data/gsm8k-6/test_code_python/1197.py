def solution():
    # Calculate the total number of beads needed for all six bracelets
    total_beads_needed = 6 * 8  # 8 beads per bracelet, 6 bracelets

    # Calculate the number of beads that Bella still needs
    beads_remaining = total_beads_needed - 36

    result = beads_remaining
    return result

print(solution())