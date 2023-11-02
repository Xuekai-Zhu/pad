def solution():
    """There are 9 boys and 12 girls in a class. The teacher needs to create groups with three members for their class activity. How many groups are formed?"""
    # Find the total number of students in the class
    total_students = 9 + 12

    # Divide the total number of students into groups of three
    num_groups = total_students // 3

    # Display the number of groups formed
    result = num_groups
    return result

print(solution())