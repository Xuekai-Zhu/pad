def solution():
    total_people = 180
    invited_couples = 20 * 2  # 20 couples from each side of family
    total_family = invited_couples * 2  # bride and groom each have 20 couples on their side
    friends_attending = total_people - total_family
    result = friends_attending
    return result

print(solution())