def solution():
    """A class has 32 students and they all need to present their projects. Every period is 40 minutes long. How many periods will it take for every student to present their project if they have 5 minutes to do so?"""
    # Define the number of students and the time needed for each presentation
    num_students = 32
    presentation_time = 5

    # Calculate the total presentation time needed for all students
    total_presentation_time = num_students * presentation_time

    # Calculate the total number of periods needed for all students to present their projects
    num_periods = total_presentation_time / 40

    # Round up to the nearest integer since partial periods are not possible
    num_periods = math.ceil(num_periods)

    # Display the number of periods needed
    result = num_periods
    return result

print(solution())