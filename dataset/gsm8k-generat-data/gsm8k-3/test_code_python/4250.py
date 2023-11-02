def solution():
    """Kingsley's teacher instructed her to find four friends to help her carry some chairs to the school hall to be used for an upcoming event.
       If each student carried 5 chairs per trip and made 10 trips in total, what's the total number of chairs taken to the hall?"""
    # Define the number of students helping Kingsley
    num_students = 4

    # Define the number of chairs each student carried per trip
    chairs_per_student = 5

    # Define the number of trips made by the students
    num_trips = 10

    # Calculate the total number of chairs taken to the hall
    total_chairs = num_students * chairs_per_student * num_trips

    # Display the total number of chairs taken to the hall
    result = total_chairs
    return result

print(solution())