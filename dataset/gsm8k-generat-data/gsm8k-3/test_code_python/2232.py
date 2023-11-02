def solution():
    """Adam goes to school every day. On Monday he had 6 lessons of 30 minutes each, and on Tuesday he had 3 lessons of 1 hour each. On Wednesday, Adam spent twice as much time at school as on Tuesday. How much time in total did Adam spend at school during these 3 days, in hours?"""
    # Define the length of each lesson in minutes
    LESSON_LENGTH = 30

    # Calculate the total time Adam spent at school on Monday
    monday_time = 6 * LESSON_LENGTH

    # Calculate the total time Adam spent at school on Tuesday
    tuesday_time = 3 * 60

    # Calculate the total time Adam spent at school on Wednesday
    wednesday_time = tuesday_time * 2

    # Calculate the total time Adam spent at school during these 3 days
    total_time = (monday_time + tuesday_time + wednesday_time) / 60

    # Display the total time in hours
    result = total_time
    return result

print(solution())