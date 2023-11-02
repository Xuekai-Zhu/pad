def solution():
    """On a particular day, Rose's teacher read the register and realized there were twice as many girls as boys present on that day. The class has 250 students, and all the 140 girls were present. If all the absent students were boys, how many boys were absent that day?"""
    # Define the total number of students and the number of girls present
    total_students = 250
    girls_present = 140

    # Calculate the number of boys present
    boys_present = (total_students - girls_present) / 3

    # Calculate the total number of boys (present + absent)
    total_boys = total_students / 3

    # Calculate the number of boys absent
    boys_absent = total_boys - boys_present

    result = boys_absent
    return result

print(solution())