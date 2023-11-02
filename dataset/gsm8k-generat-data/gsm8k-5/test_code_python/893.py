def solution():
    # Calculate the number of beads used to make the necklaces
    necklaces = 10 + 2  # Kylie makes 10 necklaces on Monday and 2 on Tuesday
    beads_per_necklace = 20  # Kylie needs 20 beads to make one necklace
    beads_used_necklaces = necklaces * beads_per_necklace

    # Calculate the number of beads used to make the bracelets
    bracelets = 5  # Kylie makes 5 bracelets on Wednesday
    beads_per_bracelet = 10  # Kylie needs 10 beads to make one bracelet
    beads_used_bracelets = bracelets * beads_per_bracelet

    # Calculate the number of beads used to make the earrings
    earrings = 7  # Kylie makes 7 earrings on Wednesday
    beads_per_earring = 5  # Kylie needs 5 beads to make one earring
    beads_used_earrings = earrings * beads_per_earring

    # Calculate the total number of beads Kylie used
    total_beads_used = beads_used_necklaces + beads_used_bracelets + beads_used_earrings
    result = total_beads_used
    return result

print(solution())