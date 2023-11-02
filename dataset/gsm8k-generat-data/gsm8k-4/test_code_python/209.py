def solution():
    """Five coaster vans are used to transport students for their field trip. Each van carries 28 students, 60 of which are boys. How many are girls?"""
    # Define the number of vans and the number of students per van
    num_vans = 5
    students_per_van = 28

    # Calculate the total number of students
    total_students = num_vans * students_per_van

    # Calculate the number of girls
    num_girls = total_students - 60

    # return the result
    result = num_girls
    return result

print(solution())