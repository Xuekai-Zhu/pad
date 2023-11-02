def solution():
    
    # Define John's normal speaking speed and training speed
    NORMAL_SPEING = 150
    TRAINING_SPEED = NORMAL_SPEING * 2.5

    # Define the number of words per page
    WORDS_PER_PAGE = 450

    # Calculate the total number of words John needs to speak
    total_words = 10 * WORDS_PER_PAGE

    # Calculate the time it would take John to speak all the words
    time_to_speak = total_words / WORDS_PER_PAGE

    # Display the time it would take John to speak all the words
    result = time_to_speak
    return result

print(solution())