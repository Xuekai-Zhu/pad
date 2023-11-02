def solution():
    """A class has 32 students and they all need to present their projects. Every period is 40 minutes long. How many periods will it take for every student to present their project if they have 5 minutes to do so?"""
    # Define the number of students and the time required to present each project
    num_students = 32
    time_per_project = 5

    # Calculate the total time required to present all projects
    total_time = num_students * time_per_project

    # Calculate the number of periods required to present all projects
    num_periods = total_time / 40

    # Round up to the nearest integer
    num_periods = int(num_periods) + 1

    result = num_periods
    return result

print(solution())