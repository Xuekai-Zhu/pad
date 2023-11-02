def solution():
    
    current_space = 8
    current_space += 2
    current_space -= 5
    current_space += 6
    spaces_left_to_win = 48 - current_space
    result = spaces_left_to_win
    return result

print(solution())