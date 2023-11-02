def solution():
    
    right_hand_speed = 10
    left_hand_speed = 7
    time = 5
    words_with_right = right_hand_speed * time
    words_with_left = left_hand_speed * time
    difference = words_with_right - words_with_left
    result = difference
    return result

print(solution())