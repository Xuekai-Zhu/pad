def solution():
    """Four adults with 32 teeth went to the dentist for a checkup after realizing they were having severe tooth pain. 
    They were found to have different numbers of damaged teeth, and each person had some teeth removed. 
    The first person had 1/4 of all his teeth removed, and the second person had 3/8 of his teeth removed, 
    the third person had half of his teeth removed, while the last person only had 4 teeth removed. 
    What's the total number of teeth removed at the dental clinic?"""
    # Define the initial number of teeth
    initial_teeth = 32

    # Calculate the number of teeth removed from the first person
    person1_teeth_removed = initial_teeth * (1/4)

    # Calculate the number of teeth remaining after the first person
    remaining_teeth1 = initial_teeth - person1_teeth_removed

    # Calculate the number of teeth removed from the second person
    person2_teeth_removed = remaining_teeth1 * (3/8)

    # Calculate the number of teeth remaining after the second person
    remaining_teeth2 = remaining_teeth1 - person2_teeth_removed

    # Calculate the number of teeth removed from the third person
    person3_teeth_removed = remaining_teeth2 * (1/2)

    # Calculate the number of teeth remaining after the third person
    remaining_teeth3 = remaining_teeth2 - person3_teeth_removed

    # Calculate the number of teeth removed from the last person
    person4_teeth_removed = 4

    # Calculate the total number of teeth removed
    total_teeth_removed = person1_teeth_removed + person2_teeth_removed + person3_teeth_removed + person4_teeth_removed

    result = total_teeth_removed
    return result

print(solution())