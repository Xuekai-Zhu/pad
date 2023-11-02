def solution():
    """Claudia offers art classes to kids and charges $10.00 for her one-hour class. If 20 kids attend Saturday’s class and half that many attend Sunday’s class, how much money does she make?"""
    # Calculate the number of kids attending Sunday's class
    sunday_kids = 20 / 2

    # Calculate the total number of kids
    total_kids = 20 + sunday_kids

    # Calculate the total earnings from both classes
    total_earnings = total_kids * 10

    result = total_earnings
    return result

print(solution())