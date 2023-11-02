def solution():
    """Mary brought 50 stickers to class. She gave 4 stickers to each of her 5 friends. She gave everyone else in class two stickers each. If she has 8 stickers left over, how many students are in the class, including Mary?"""
    # Define the number of stickers Mary gave to each friend
    friend_stickers = 4

    # Calculate how many stickers Mary gave to her friends
    friend_total = friend_stickers * 5

    # Calculate how many stickers Mary gave to the rest of the class
    rest_total = 50 - friend_total - 8

    # Calculate how many students are in the class, including Mary
    student_total = 5 + (rest_total // 2) + 1

    # Display the total number of students
    result = student_total
    return result

print(solution())