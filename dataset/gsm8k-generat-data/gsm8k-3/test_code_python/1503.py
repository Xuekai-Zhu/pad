def solution():
    """Jerome has 20 classmates on his cell phone contact list.  He has half as many out of school friends as classmates on his contact list.  He also has his two parents and his sister on his contact list.  How many people are on Jerome's contact list?"""
    # Define the number of classmates and the number of out of school friends
    classmates = 20
    out_of_school_friends = classmates / 2

    # Define the number of family members
    family_members = 4  # Jerome's two parents and his sister

    # Calculate the total number of contacts on Jerome's list
    total_contacts = classmates + out_of_school_friends + family_members

    # Display the total number of contacts
    result = total_contacts
    return result

print(solution())