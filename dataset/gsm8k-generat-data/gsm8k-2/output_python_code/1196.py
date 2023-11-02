def solution():
    """Bella is making bracelets for her 6 friends. She needs 8 beads per bracelet. She has 36 beads. How many more beads does she need to make all six bracelets?"""
    beads_per_bracelet = 8
    total_bracelets = 6
    total_beads_needed = beads_per_bracelet * total_bracelets
    beads_remaining = total_beads_needed - 36
    result = beads_remaining
    return result

print(solution())