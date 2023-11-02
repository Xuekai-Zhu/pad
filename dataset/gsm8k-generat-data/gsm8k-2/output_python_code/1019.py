def solution():
    """Matt can write 10 words a minute with his right hand and 7 words a minute with his left hand. How many words would Matt write in 5 minutes with his right hand than with his left?"""
    right_hand_speed = 10
    left_hand_speed = 7
    time = 5
    words_with_right = right_hand_speed * time
    words_with_left = left_hand_speed * time
    difference = words_with_right - words_with_left
    result = difference
    return result

print(solution())