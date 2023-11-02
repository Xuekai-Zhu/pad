def solution():
    """Janice can type 6 sentences per minute. Today at work, Janice continued working on a paper she started typing yesterday. She typed for 20 minutes, took a break, and typed 15 minutes longer. She then had to erase 40 sentences she had typed incorrectly. After a meeting, she typed for 18 minutes more. In all, the paper had 536 sentences by the end of today. How many sentences did she start with today?"""
    # Define the typing speed
    typing_speed = 6 # sentences per minute

    # Calculate the total time spent typing
    total_typing_time = 20 + 15 + 18 # minutes

    # Calculate the total number of sentences typed
    total_sentences_typed = total_typing_time * typing_speed

    # Subtract the number of sentences erased
    total_sentences_typed -= 40

    # Add the number of sentences at the end of today
    total_sentences_typed += 536

    # Subtract the number of sentences already typed yesterday
    initial_sentences = total_sentences_typed - (typing_speed * 60 * 24)

    # Return the result
    result = initial_sentences
    return result

print(solution())