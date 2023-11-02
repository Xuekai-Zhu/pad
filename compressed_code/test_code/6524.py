def solution():
    
    friends_from_school = 6
    friends_from_neighborhood = 12
    new_friends_per_person = 2
    total_people = friends_from_school + friends_from_neighborhood + (friends_from_school + friends_from_neighborhood) * new_friends_per_person
    result = total_people
    return result

print(solution())