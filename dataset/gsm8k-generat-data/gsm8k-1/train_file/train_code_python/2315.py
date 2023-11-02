def solution():
    """Mary brought 50 stickers to class. She gave 4 stickers to each of her 5 friends. She gave everyone else in class two stickers each. If she has 8 stickers left over, how many students are in the class, including Mary?"""
    initial_stickers = 50
    friends = 5
    friend_stickers = 4
    remaining_stickers = initial_stickers - (friends * friend_stickers)
    other_stickers = remaining_stickers - 8
    other_students = other_stickers // 2
    total_students = friends + 1 + other_students
    result = total_students
    return result

print(solution())