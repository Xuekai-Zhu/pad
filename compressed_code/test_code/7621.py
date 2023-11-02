def solution():
    
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