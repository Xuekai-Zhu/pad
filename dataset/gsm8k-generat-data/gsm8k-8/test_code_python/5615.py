def solution():
    # Define the initial number of phones
    initial_phones = 15

    # Define the number of phones repaired by Kevin
    kevin_repaired = 3

    # Define the number of new phones brought in
    new_phones = 6

    # Calculate the total number of phones by adding the initial, repaired, and new phones
    total_phones = initial_phones + kevin_repaired + new_phones

    # Calculate the number of phones each person needs to repair by dividing the total by 2 (since there are now 2 people working)
    phones_per_person = total_phones / 2
    result = phones_per_person
    return result

print(solution())