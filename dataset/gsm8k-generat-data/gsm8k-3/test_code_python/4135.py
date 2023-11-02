def solution():
    """Four adults with 32 teeth went to the dentist for a checkup after realizing they were having severe tooth pain. They were found to have different numbers of damaged teeth, and each person had some teeth removed. The first person had 1/4 of all his teeth removed, and the second person had 3/8 of his teeth removed, the third person had half of his teeth removed, while the last person only had 4 teeth removed. What's the total number of teeth removed at the dental clinic?"""
    # Define the number of teeth each person had
    person1_teeth = 32
    person2_teeth = 32
    person3_teeth = 32
    person4_teeth = 32

    # Calculate the number of teeth removed for each person
    person1_removed = person1_teeth * 1/4
    person2_removed = person2_teeth * 3/8
    person3_removed = person3_teeth * 1/2
    person4_removed = 4

    # Calculate the total number of teeth removed
    total_removed = person1_removed + person2_removed + person3_removed + person4_removed

    # Display the total number of teeth removed
    result = total_removed
    return result

print(solution())