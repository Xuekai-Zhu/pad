def solution():
    """A couple's wedding reception had 180 people. The bride and groom had each invited 20 couples from their side of the family. The remaining guests were friends. How many friends attended the reception?"""
    # Define the number of couples invited from each side of the family
    couples_per_side = 20

    # Calculate the number of people invited from each side of the family
    family_members_per_side = couples_per_side * 2

    # Calculate the total number of family members invited
    total_family_members = family_members_per_side * 2

    # Calculate the number of friends who attended the reception
    friends_attending = 180 - total_family_members

    # return the result
    result = friends_attending
    return result

print(solution())