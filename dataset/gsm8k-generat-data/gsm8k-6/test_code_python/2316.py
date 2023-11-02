def solution():
    # Calculate the total number of stickers given to Mary's 5 friends
    stickers_given_to_friends = 4 * 5

    # Calculate the total number of stickers given to everyone else in class
    stickers_given_to_class = (50 - stickers_given_to_friends - 8)

    # Calculate the number of students in the class, including Mary
    total_students = 6 + (stickers_given_to_class // 2)

    result = total_students
    return result

print(solution())