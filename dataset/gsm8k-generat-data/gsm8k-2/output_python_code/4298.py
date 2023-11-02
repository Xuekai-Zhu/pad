def solution():
    """Kelsey had 2/5 of a tray of eggs that she had brought to Willa's party.
    Stephanie had also brought half a tray of eggs to the party, while Alayah
    brought 40 more eggs than Kelsey and Stephanie combined. If Willa had two
    trays of eggs already, calculate the total number of eggs that were used at
    the party."""
    kelsey_eggs = 2/5
    stephanie_eggs = 1/2
    combined_eggs = kelsey_eggs + stephanie_eggs
    alayah_eggs = combined_eggs + 40
    total_eggs = 2 + kelsey_eggs + stephanie_eggs + alayah_eggs
    result = total_eggs
    return result

print(solution())