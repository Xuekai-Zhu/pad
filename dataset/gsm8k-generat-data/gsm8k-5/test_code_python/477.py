def solution():
    couples_invited = 20 + 20  # Both bride and groom invited 20 couples each
    total_invited = couples_invited * 2  # Total number of guests from family
    friends_attending = 180 - total_invited  # Remaining guests were friends
    result = friends_attending
    return result

print(solution())