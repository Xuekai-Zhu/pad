def solution():
    """Kelly needs school supplies to teach her class for an art project. She has 8 students and they will need 3 pieces of construction paper each. In addition to the construction paper, she needs to buy 6 bottles of glue for everyone to share. After Kelly purchases these supplies, she dropped half of them down a storm drain. Class is about to start, but she manages to rush to the store and buy 5 more pieces of construction paper. How many supplies are left?"""
    # Define the number of students and pieces of construction paper needed per student
    NUM_STUDENTS = 8
    PAPER_PER_STUDENT = 3

    # Calculate the total number of pieces of construction paper needed
    total_paper_needed = NUM_STUDENTS * PAPER_PER_STUDENT

    # Define the number of bottles of glue needed
    NUM_GLUE = 6

    # Calculate the total number of supplies needed
    total_supplies = total_paper_needed + NUM_GLUE

    # Calculate the number of supplies left after dropping half and buying 5 more pieces of construction paper
    remaining_supplies = (total_supplies / 2) + 5

    result = remaining_supplies
    return result

print(solution())