def solution():
    guests = 30  # Patsy has 30 guests
    appetizers_per_guest = 6  # Patsy needs 6 appetizers per guest
    total_appetizers_needed = guests * appetizers_per_guest  # Calculate the total number of appetizers needed

    deviled_eggs = 3 * 12  # Patsy is making 3 dozen (3 x 12) deviled eggs
    pigs_in_a_blanket = 2 * 12  # Patsy is making 2 dozen (2 x 12) pigs in a blanket
    kebabs = 2 * 12  # Patsy is making 2 dozen (2 x 12) kebabs
    total_appetizers_made = deviled_eggs + pigs_in_a_blanket + kebabs  # Calculate the total number of appetizers made

    # Calculate the number of more dozens of appetizers Patsy needs to make to meet the required number of appetizers
    more_appetizers_needed = (total_appetizers_needed - total_appetizers_made) / 12
    result = more_appetizers_needed
    return result

print(solution())