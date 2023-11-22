def solution():
    
    # Define the number of teachers and lessons per day
    num_teachers = 4
    lessons_per_teacher = 2

    # Calculate the total number of lessons per day
    total_lessons = num_teachers * lessons_per_teacher

    # Calculate the total number of times the whiteboard is cleaned in a day
    cleaned_times = total_lessons * 3

    # Display the number of times the whiteboard is cleaned in a day
    result = cleaned_times
    return result

print(solution())