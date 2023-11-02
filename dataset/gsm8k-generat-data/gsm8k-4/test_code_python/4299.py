def solution():
    """Kelsey had 2/5 of a tray of eggs that she had brought to Willa's party. Stephanie had also brought half a tray of eggs to the party, while Alayah brought 40 more eggs than Kelsey and Stephanie combined. If Willa had two trays of eggs already, calculate the total number of eggs that were used at the party."""
    # Calculate the number of eggs Kelsey brought to the party
    kelsey_eggs = 2/5 * 30 # 30 eggs per tray

    # Calculate the number of eggs Stephanie brought to the party
    stephanie_eggs = 1/2 * 30 # 30 eggs per tray

    # Calculate the number of eggs Alayah brought to the party
    alayah_eggs = kelsey_eggs + stephanie_eggs + 40

    # Calculate the total number of eggs at the party
    total_eggs = (2 * 30) + kelsey_eggs + stephanie_eggs + alayah_eggs

    # return the result
    result = total_eggs
    return result

print(solution())