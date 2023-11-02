def solution():
    """Kelsey had 2/5 of a tray of eggs that she had brought to Willa's party. Stephanie had also brought half a tray of eggs to the party, while Alayah brought 40 more eggs than Kelsey and Stephanie combined. If Willa had two trays of eggs already, calculate the total number of eggs that were used at the party."""
    # Define the fraction of a tray of eggs Kelsey brought
    kelsey_eggs = 2/5

    # Define the number of eggs Stephanie brought (assuming a tray has 12 eggs)
    stephanie_eggs = 12 * 0.5

    # Calculate the total number of eggs Kelsey and Stephanie brought
    total_eggs = 12 * (kelsey_eggs + stephanie_eggs)

    # Calculate the number of eggs Alayah brought
    alayah_eggs = total_eggs + 40

    # Calculate the total number of eggs at the party
    total_party_eggs = 12*2 + total_eggs + alayah_eggs

    # Display the total number of eggs used at the party
    result = total_party_eggs
    return result

print(solution())