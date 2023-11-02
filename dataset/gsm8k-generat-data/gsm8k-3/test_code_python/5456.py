def solution():
    """There are 100 students in class and the ratio of boys to girls is 3:2. How many more boys than girls are there?"""
    # Define the ratio of boys to girls
    BOY_GIRL_RATIO = 3/2

    # Calculate the number of boys and girls based on the ratio and total number of students
    total_students = 100
    boy_count = total_students * (BOY_GIRL_RATIO / (BOY_GIRL_RATIO + 1))
    girl_count = total_students * (1 / (BOY_GIRL_RATIO + 1))

    # Calculate the difference between the number of boys and girls
    difference = boy_count - girl_count

    # Display the difference
    result = difference
    return result

print(solution())