def solution():
    """Matt can write 10 words a minute with his right hand and 7 words a minute with his left hand. How many words would Matt write in 5 minutes with his right hand than with his left?"""
    # Define the writing speeds
    right_speed = 10  # words per minute
    left_speed = 7  # words per minute

    # Calculate the number of words Matt can write with each hand in 5 minutes
    right_words = right_speed * 5
    left_words = left_speed * 5

    # Calculate the difference between the number of words written with each hand
    difference = right_words - left_words

    # return the result
    result = difference
    return result

print(solution())