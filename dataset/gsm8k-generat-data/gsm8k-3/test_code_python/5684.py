def solution():
    """The kindergartners each need to bring one mini tissue box to class for the school year.  There are three kindergartner groups with 9, 10, and 11 students respectively.  Each mini tissue box contains 40 tissues.  How many tissues do the kindergartner groups bring together?"""
    # Define the number of students in each group
    group1 = 9
    group2 = 10
    group3 = 11

    # Define the number of tissues in each mini tissue box
    tissues_per_box = 40

    # Calculate the total number of tissues brought by all the groups
    total_tissues = (group1 + group2 + group3) * tissues_per_box

    # Display the total number of tissues
    result = total_tissues
    return result

print(solution())