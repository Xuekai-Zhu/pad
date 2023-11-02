def solution():
    """On a particular day, Rose's teacher read the register and realized there were twice as many girls as boys present on that day. 
    The class has 250 students, and all the 140 girls were present. If all the absent students were boys, how many boys were absent that day?"""
    
    # Calculate the total number of boys in the class
    total_students = 250
    total_girls = 140
    total_boys = (total_students - total_girls) / 3

    # Calculate the number of absent boys
    present_girls = total_girls
    present_boys = total_boys * 2
    present_students = present_girls + present_boys
    absent_students = total_students - present_students
    absent_boys = absent_students / 3

    # Display the number of absent boys
    result = absent_boys
    return result

print(solution())