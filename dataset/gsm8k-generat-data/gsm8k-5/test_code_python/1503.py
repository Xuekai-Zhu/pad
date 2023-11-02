def solution():
    classmates = 20  # Jerome has 20 classmates on his contact list
    out_of_school_friends = classmates / 2  # Jerome has half as many out of school friends as classmates
    total_contacts = classmates + out_of_school_friends + 3  # Jerome also has his parents and sister on his contact list
    result = total_contacts
    return result

print(solution())