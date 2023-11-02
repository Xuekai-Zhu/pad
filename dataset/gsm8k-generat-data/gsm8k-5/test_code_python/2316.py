def solution():
    total_stickers = 50  # Mary brought 50 stickers to class
    friends = 5  # Mary gave stickers to 5 friends
    friend_stickers = 4  # Mary gave 4 stickers to each friend

    # Calculate the total number of stickers given to friends
    total_friend_stickers = friends * friend_stickers

    # Calculate the stickers remaining after giving friends their stickers
    remaining_stickers = total_stickers - total_friend_stickers

    # Calculate the number of students who are not friends
    other_students = (remaining_stickers - 8) / 2

    # Calculate the total number of students, including Mary
    total_students = 1 + friends + other_students
    result = total_students
    return result

print(solution())