def solution():
    """In a graduation ceremony, each graduate can bring their 2 parents. Twenty teachers and half as many administrators will also attend the graduation ceremony. If there are 50 graduates, how many chairs must be prepared for the ceremony?"""
    # Define the number of chairs needed per graduate
    CHAIRS_PER_GRADUATE = 3

    # Calculate the number of chairs needed for the graduates and their parents
    graduate_chairs = 50 * CHAIRS_PER_GRADUATE

    # Calculate the number of chairs needed for the teachers and administrators
    teacher_chairs = 20
    admin_chairs = teacher_chairs//2

    # Calculate the total number of chairs needed
    total_chairs = graduate_chairs + teacher_chairs + admin_chairs

    # Display the total number of chairs needed
    result = total_chairs
    return result

print(solution())