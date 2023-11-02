def solution():
    # Calculate the number of people invited from the bride and groom's side
    invited_from_family = 20 * 2

    # Subtract the number of family members from the total number of guests to get the number of friends
    friends_attended = 180 - invited_from_family

    result = friends_attended
    return result

print(solution())