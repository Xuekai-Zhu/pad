def solution():
    # Calculate the total words Matt can write with his right hand in 5 minutes
    right_hand_words = 10 * 5

    # Calculate the total words Matt can write with his left hand in 5 minutes
    left_hand_words = 7 * 5

    # Calculate the difference between the two
    difference = right_hand_words - left_hand_words
    result = difference
    return result

print(solution())