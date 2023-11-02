def solution():
    friends = 6  # Bella is making bracelets for 6 friends
    beads_per_bracelet = 8  # Bella needs 8 beads per bracelet
    total_beads_needed = friends * beads_per_bracelet  # Bella needs this many beads in total

    # Calculate how many more beads Bella needs to make all six bracelets
    additional_beads_needed = total_beads_needed - 36

    result = additional_beads_needed
    return result

print(solution())