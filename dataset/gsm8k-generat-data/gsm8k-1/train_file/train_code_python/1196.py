def solution():
    """Bella is making bracelets for her 6 friends. She needs 8 beads per bracelet. She has 36 beads. How many more beads does she need to make all six bracelets?"""
    beads_per_bracelet = 8
    total_beads_needed = beads_per_bracelet * 6
    beads_available = 36
    beads_needed = total_beads_needed - beads_available
    result = beads_needed
    return result

print(solution())