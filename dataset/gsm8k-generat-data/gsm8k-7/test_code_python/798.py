def solution():
    num_guests = 30
    appetizers_per_guest = 6

    deviled_eggs_per_dozen = 12
    num_deviled_egg_dozen = 3

    pigs_in_blanket_per_dozen = 12
    num_pigs_in_blanket_dozen = 2

    kebabs_per_dozen = 12
    num_kebab_dozen = 2

    # Calculate the total number of appetizers needed
    total_appetizers_needed = num_guests * appetizers_per_guest

    # Calculate the total number of appetizers that have already been made
    total_appetizers_made = (num_deviled_egg_dozen * deviled_eggs_per_dozen) + (num_pigs_in_blanket_dozen * pigs_in_blanket_per_dozen) + (num_kebab_dozen * kebabs_per_dozen)

    # Calculate the number of dozen appetizers that still need to be made
    num_dozen_to_make = (total_appetizers_needed - total_appetizers_made) / 12
    result = num_dozen_to_make
    return result

print(solution())