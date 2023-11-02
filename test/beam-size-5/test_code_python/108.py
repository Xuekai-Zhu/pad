def solution():
    
    # Define the number of teachers and lessons per day
    NUM_TEACHERS = 4
    LESSONS_PER_TEACHER = 2

    # Define the number of times the whiteboard is cleaned per lesson
    WHITEBOARDS_PER_LESSON = 3

    # Calculate the number of lessons per day
    lessons_per_day = NUM_TEACHERS * LESSONS_PER_TEACHER

    # Calculate the number of times the whiteboard is cleaned in a day
    clean_times_per_day = lessons_per_day * WHITEBOARDS_PER_LESSON

    # Display the number of times the whiteboard is cleaned in a day
    result = clean_times_per_day
    return result

print(solution())