def solution():
    """A couple's wedding reception had 180 people. The bride and groom had each invited 20 couples from their side of the family. The remaining guests were friends. How many friends attended the reception?"""
    couples_invited_from_family = 20
    total_couples_invited = couples_invited_from_family * 2
    total_family_members = total_couples_invited * 2
    total_guests = 180
    friends_attending = total_guests - total_family_members
    result = friends_attending
    return result

print(solution())