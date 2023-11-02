def solution():
    """Kelly needs school supplies to teach her class for an art project. She has 8 students and they will need 3 pieces of construction paper each. In addition to the construction paper, she needs to buy 6 bottles of glue for everyone to share. After Kelly purchases these supplies, she dropped half of them down a storm drain. Class is about to start, but she manages to rush to the store and buy 5 more pieces of construction paper. How many supplies are left?"""
    # Define the number of students and the number of pieces of construction paper needed per student
    num_students = 8
    num_paper_per_student = 3

    # Calculate the total number of pieces of construction paper needed
    total_paper_needed = num_students * num_paper_per_student

    # Add the number of bottles of glue needed
    total_supplies_needed = total_paper_needed + 6

    # Calculate the number of supplies remaining after half are lost and 5 more pieces of paper are bought
    remaining_supplies = total_supplies_needed / 2 + 5

    # Return the result
    result = remaining_supplies
    return result

print(solution())