def solution():
    """Mary brought 50 stickers to class. She gave 4 stickers to each of her 5 friends. She gave everyone else in class two stickers each. If she has 8 stickers left over, how many students are in the class, including Mary?"""
    # Define the number of stickers Mary brought
    stickers = 50

    # Define the number of friends Mary has
    friends = 5

    # Calculate the number of stickers given to friends
    stickers_friends = friends * 4

    # Calculate the number of stickers left for the rest of the class
    stickers_rest = stickers - stickers_friends - 8

    # Calculate the number of students in the class, including Mary
    students = friends + (stickers_rest // 2) + 1

    # return the result
    result = students
    return result

print(solution())