def solution():
    """Adam goes to school every day. On Monday he had 6 lessons of 30 minutes each, and on Tuesday he had 3 lessons of 1 hour each. On Wednesday, Adam spent twice as much time at school as on Tuesday. How much time in total did Adam spend at school during these 3 days, in hours?"""
    # Define the duration of Adam's lessons in minutes
    monday_lesson_duration = 30
    tuesday_lesson_duration = 60

    # Calculate the total duration of Adam's lessons on Monday and Tuesday
    monday_duration = 6 * monday_lesson_duration
    tuesday_duration = 3 * tuesday_lesson_duration

    # Calculate the duration of Adam's lessons on Wednesday
    wednesday_duration = tuesday_duration * 2

    # Calculate the total time Adam spent at school in minutes
    total_duration = monday_duration + tuesday_duration + wednesday_duration

    # Convert the total duration to hours
    total_hours = total_duration / 60

    # return the result
    result = total_hours
    return result

print(solution())