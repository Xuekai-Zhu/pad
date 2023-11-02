def solution():
    """A teacher is making packed lunches for a field trip. Each student needs 2 sandwiches, and will travel in a group with 5 other students. There are a total of 5 groups. How many pieces of bread will the teacher need to make enough sandwiches for all the students?"""

    # Define the number of students in each group
    students_per_group = 6

    # Determine the total number of students
    total_students = students_per_group * 5

    # Calculate the total number of sandwiches needed
    sandwiches_needed = total_students * 2

    # Calculate the total number of pieces of bread needed
    bread_needed = sandwiches_needed * 2

    result = bread_needed
    return result

print(solution())