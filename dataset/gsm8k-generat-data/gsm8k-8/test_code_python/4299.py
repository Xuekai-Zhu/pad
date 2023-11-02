def solution():
    # Define the fractions of the tray of eggs
    kelsey_fraction = 2/5
    stephanie_fraction = 1/2

    # Calculate the total number of eggs Kelsey and Stephanie brought
    kelsey_and_stephanie_eggs = 2/5 + 1/2

    # Calculate the number of eggs Alayah brought
    alayah_eggs = kelsey_and_stephanie_eggs + 40

    # Calculate the total number of trays of eggs at the party
    total_trays = 2 + (kelsey_fraction + stephanie_fraction + alayah_eggs)/12

    # Calculate the total number of eggs at the party
    total_eggs = total_trays * 12

    result = total_eggs
    return result

print(solution())