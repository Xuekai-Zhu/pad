def solution():
    """The kindergartners each need to bring one mini tissue box to class for the school year. There are three kindergartner groups with 9, 10, and 11 students respectively. Each mini tissue box contains 40 tissues. How many tissues do the kindergartner groups bring together?"""
    
    # Define the number of students in each group
    group1_students = 9
    group2_students = 10
    group3_students = 11
    
    # Define the number of tissues in each mini tissue box
    tissues_per_box = 40
    
    # Calculate the total number of tissues needed
    total_tissues = (group1_students + group2_students + group3_students) * tissues_per_box
    
    # return the result
    result = total_tissues
    return result

print(solution())