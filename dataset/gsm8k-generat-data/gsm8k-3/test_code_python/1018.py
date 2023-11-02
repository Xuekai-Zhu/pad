def solution():
    """Ron is part of a book club that allows each member to take a turn picking a new book every week. 
    The club is made up of three couples and five single people along with Ron and his wife. 
    How many times a year does Ron get to pick a new book?"""
    # Define the number of couples and single people in the book club
    NUM_COUPLES = 3
    NUM_SINGLE = 5

    # Define the number of members in the book club, including Ron and his wife
    NUM_MEMBERS = 1 + 1 + (NUM_COUPLES * 2) + NUM_SINGLE

    # Calculate how many times Ron gets to pick a new book each year
    RON_PICKS_PER_YEAR = int(52 / NUM_MEMBERS)

    # Display the number of times Ron gets to pick a new book each year
    result = RON_PICKS_PER_YEAR
    return result

print(solution())