def solution():
    
    # Define John's normal speaking speed and the speed after training
    NORMAL_SPEED = 150
    TRAINING_SPEED = NORMAL_SPEED * 2.5

    # Define the number of words per page
    WORDS_PER_PAGE = 450

    # Define the number of pages to be sold
    PAGES_TO_SPEED = 10

    # Calculate the total number of words to be speak
    total_words = PAGES_TO_SPEED * WORDS_PER_PAGE

    # Calculate the time it will take John to speak all the words
    time_in_minutes = total_words / WORDS_PER_PAGE

    # Display the time it will take John to speak all the words
    result = time_in_minutes
    return result

print(solution())