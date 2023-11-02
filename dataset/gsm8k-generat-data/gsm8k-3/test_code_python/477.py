def solution():
    """A couple's wedding reception had 180 people. The bride and groom had each invited 20 couples from their side of the family. The remaining guests were friends. How many friends attended the reception?"""
    # Calculate the number of people invited from the family
    family_invited = 20 * 2 # 20 couples from each side of the family, so 20 * 2 = 40 people

    # Subtract the number of family members from the total number of guests to get the number of friends
    friends_attended = 180 - family_invited

    # Display the number of friends who attended the reception
    result = friends_attended
    return result

print(solution())