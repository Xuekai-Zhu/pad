def solution():
    """Jerome has 20 classmates on his cell phone contact list. He has half as many out of school friends as classmates on his contact list. He also has his two parents and his sister on his contact list. How many people are on Jerome's contact list?"""
    # Define the number of classmates
    classmates = 20

    # Define the number of out of school friends
    friends = classmates / 2

    # Add the family members to the contact list
    contact_list = classmates + friends + 2 + 1

    # Return the result
    result = contact_list
    return result

print(solution())