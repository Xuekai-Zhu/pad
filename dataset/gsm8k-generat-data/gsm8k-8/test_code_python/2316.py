def solution():
    # Calculate the total number of stickers Mary gave to her friends
    friend_sticker_total = 4 * 5

    # Calculate the remaining number of stickers Mary gave to other students
    other_sticker_remaining = 50 - friend_sticker_total - 8

    # Calculate the number of students other than Mary in the class
    other_students = other_sticker_remaining / 2

    # Calculate the total number of students, including Mary
    total_students = other_students + 5 + 1

    result = total_students
    return result

print(solution())