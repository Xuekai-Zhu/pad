def solution():
    # Calculate the number of cans needed to feed 40 people
    cans_per_person = 600/40
    # Calculate the number of people in the 30% fewer group
    new_group_size = (100 - 30)/100 * 40
    # Calculate the number of cans needed to feed the new group
    new_total_cans = new_group_size * cans_per_person
    result = new_total_cans
    return result

print(solution())