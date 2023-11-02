def solution():
    
    mary_stickers = 50
    num_friends = 5
    friend_stickers = 4
    remaining_stickers = 8
    friend_total_stickers = num_friends * friend_stickers
    remaining_students = (mary_stickers - friend_total_stickers - remaining_stickers) / 2
    total_students = num_friends + remaining_students + 1
    result = total_students
    return result

print(solution())