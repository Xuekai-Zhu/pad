def solution():
    
    oranges = 12
    brother_oranges = oranges // 3
    remaining_oranges = oranges - brother_oranges
    friend_oranges = remaining_oranges // 4
    result = friend_oranges
    return result

print(solution())