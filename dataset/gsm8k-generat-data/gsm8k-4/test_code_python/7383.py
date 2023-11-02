def solution():
    """There are 9 boys and 12 girls in a class. The teacher needs to create groups with three members for their class activity. How many groups are formed?"""
    # Define the number of boys and girls in the class
    num_boys = 9
    num_girls = 12

    # Calculate the total number of students in the class
    total_students = num_boys + num_girls

    # Calculate the number of groups that can be formed
    num_groups = total_students // 3

    # Return the result
    result = num_groups
    return result

print(solution())