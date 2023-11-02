def solution():
    """Micah can type 20 words per minute and Isaiah can type 40 words per minute. How many more words can Isaiah type than Micah in an hour?"""
    # Define the typing speed of Micah and Isaiah
    MICAH_SPEED = 20
    ISAIAH_SPEED = 40

    # Calculate the number of words Micah can type in an hour
    micah_words = MICAH_SPEED * 60

    # Calculate the number of words Isaiah can type in an hour
    isaiah_words = ISAIAH_SPEED * 60

    # Calculate the difference in the number of words they can type in an hour
    difference = isaiah_words - micah_words

    # Display the difference
    result = difference
    return result

print(solution())