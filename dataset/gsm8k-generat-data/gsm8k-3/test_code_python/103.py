def solution():
    """Janice can type 6 sentences per minute. Today at work, Janice continued working on a paper she started typing yesterday. She typed for 20 minutes, took a break, and typed 15 minutes longer. She then had to erase 40 sentences she had typed incorrectly. After a meeting, she typed for 18 minutes more. In all, the paper had 536 sentences by the end of today. How many sentences did she start with on today?"""
    # Define the typing speed in sentences per minute
    SPEED = 6

    # Calculate the total time spent typing
    total_time = 20 + 15 + 18

    # Calculate the total number of sentences typed
    total_sentences = 536 + 40

    # Calculate the number of sentences typed during the total time
    typed_sentences = SPEED * total_time

    # Calculate the number of sentences Janice started with
    start_sentences = total_sentences - typed_sentences

    result = start_sentences
    return result

print(solution())