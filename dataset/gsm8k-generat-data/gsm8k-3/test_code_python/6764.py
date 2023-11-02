def solution():
    """A teacher is making packed lunches for a field trip. Each student needs 2 sandwiches, and will travel in a group with 5 other students. There are a total of 5 groups. How many pieces of bread will the teacher need to make enough sandwiches for all the students?"""
    # Define the number of students per group and the number of groups
    STUDENTS_PER_GROUP = 6
    NUM_GROUPS = 5

    # Calculate the total number of students
    total_students = STUDENTS_PER_GROUP * NUM_GROUPS

    # Calculate the total number of sandwiches needed
    sandwiches_needed = total_students * 2

    # Calculate the total number of bread slices needed
    bread_slices_needed = sandwiches_needed * 2

    # Display the total number of bread slices needed
    result = bread_slices_needed
    return result

print(solution())