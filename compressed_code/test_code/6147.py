def solution():
    
    couples_invited_from_family = 20
    total_couples_invited = couples_invited_from_family * 2
    total_family_members = total_couples_invited * 2
    total_guests = 180
    friends_attending = total_guests - total_family_members
    result = friends_attending
    return result

print(solution())