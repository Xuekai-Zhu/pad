def solution():
    """Kelly needs school supplies to teach her class for an art project. She has 8 students and they will need 3 pieces of construction paper each. In addition to the construction paper, she needs to buy 6 bottles of glue for everyone to share. After Kelly purchases these supplies, she dropped half of them down a storm drain. Class is about to start, but she manages to rush to the store and buy 5 more pieces of construction paper. How many supplies are left?"""
    students = 8
    paper_per_student = 3
    glue_bottles = 6
    total_paper = students * paper_per_student + glue_bottles
    lost_supplies = total_paper / 2
    additional_paper = 5
    remaining_supplies = total_paper - lost_supplies + additional_paper
    result = remaining_supplies
    return result

print(solution())