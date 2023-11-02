def solution():
    """Before Cameron broke his right arm, he was able to type 10 words per minute on his phone. After he broke his arm, he had to use his left hand for a while, and he could only type 8 words per minute. What is the difference between the number of words he could type in 5 minutes before and after he broke his arm?"""
    # Define Cameron's typing speed before and after he broke his arm
    BEFORE_SPEED = 10
    AFTER_SPEED = 8

    # Define the amount of time Cameron typed for
    TIME = 5

    # Calculate the number of words Cameron could type before and after he broke his arm
    before_words = BEFORE_SPEED * TIME
    after_words = AFTER_SPEED * TIME

    # Calculate the difference in the number of words Cameron could type before and after he broke his arm
    difference = before_words - after_words

    # Display the difference
    result = difference
    return result

print(solution())