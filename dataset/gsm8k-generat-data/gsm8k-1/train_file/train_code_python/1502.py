def solution():
    """Jerome has 20 classmates on his cell phone contact list. He has half as many out of school friends as classmates on his contact list. He also has his two parents and his sister on his contact list. How many people are on Jerome's contact list?"""
    classmates = 20
    out_of_school_friends = classmates / 2
    parents = 2
    sister = 1
    total_contacts = classmates + out_of_school_friends + parents + sister
    result = total_contacts
    return result

print(solution())