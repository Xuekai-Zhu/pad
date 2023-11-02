def solution():
    # Calculate the total number of people on Jerome's contact list
    classmates = 20
    out_of_school_friends = classmates / 2
    family_members = 4  # Jerome's 2 parents and 1 sister (assuming Jerome himself is not on his own contact list)
    total_contacts = classmates + out_of_school_friends + family_members
    result = total_contacts
    return result

print(solution())