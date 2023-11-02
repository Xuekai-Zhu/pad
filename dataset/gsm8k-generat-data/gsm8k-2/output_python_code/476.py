def solution():
    """A couple's wedding reception had 180 people. The bride and groom had each invited 20 couples from their side of the family. The remaining guests were friends. How many friends attended the reception?"""
    total_couples_invited = 20 + 20
    total_people_invited = total_couples_invited * 2
    friends_attended = 180 - total_people_invited
    result = friends_attended
    return result

print(solution())