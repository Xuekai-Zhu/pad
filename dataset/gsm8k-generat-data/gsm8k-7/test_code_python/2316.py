def solution():
    total_stickers = 50
    num_friends = 5
    stickers_per_friend = 4
    stickers_per_student = 2
    leftover_stickers = 8

    # Calculate the total number of stickers given to friends
    total_friend_stickers = num_friends * stickers_per_friend

    # Calculate the total number of stickers given to other students
    total_other_stickers = total_stickers - total_friend_stickers - leftover_stickers

    # Calculate the number of other students in class
    num_other_students = total_other_stickers / stickers_per_student

    # Calculate the total number of students, including Mary
    total_students = num_friends + num_other_students + 1
    result = total_students
    return result

print(solution())