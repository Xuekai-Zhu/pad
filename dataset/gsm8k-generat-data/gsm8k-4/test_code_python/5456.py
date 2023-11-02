def solution():
    """There are 100 students in class and the ratio of boys to girls is 3:2. How many more boys than girls are there?"""
    # Define the total number of students and the ratio of boys to girls
    total_students = 100
    boy_to_girl_ratio = 3/2

    # Calculate the number of boys and girls
    boys = total_students / (boy_to_girl_ratio + 1.0) * boy_to_girl_ratio
    girls = total_students - boys

    # Calculate the difference between the number of boys and girls
    difference = boys - girls

    # return the result
    result = difference
    return result

print(solution())