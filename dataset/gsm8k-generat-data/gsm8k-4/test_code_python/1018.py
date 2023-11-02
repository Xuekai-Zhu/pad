def solution():
    """Ron is part of a book club that allows each member to take a turn picking a new book every week. The club is made up of three couples and five single people along with Ron and his wife. How many times a year does Ron get to pick a new book?"""
    # Define the total number of members in the club
    total_members = 3*2 + 5 + 2

    # Calculate how often Ron gets to pick a book
    ron_picks = 1 / total_members * 52

    # return the result
    result = round(ron_picks)
    return result

print(solution())