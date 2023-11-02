def solution():
    """Matt can write 10 words a minute with his right hand and 7 words a minute with his left hand. How many words would Matt write in 5 minutes with his right hand than with his left?"""
    # Define Matt's writing speeds in words per minute
    RIGHT_SPEED = 10
    LEFT_SPEED = 7

    # Calculate the number of words Matt can write in 5 minutes with each hand
    right_words = RIGHT_SPEED * 5
    left_words = LEFT_SPEED * 5

    # Calculate the difference in the number of words Matt can write in 5 minutes with his right hand vs. his left hand
    word_difference = right_words - left_words

    # Display the difference in the number of words Matt can write in 5 minutes with his right hand vs. his left hand
    result = word_difference
    return result

print(solution())