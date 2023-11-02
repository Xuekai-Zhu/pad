def solution():
    """Kelly needs school supplies to teach her class for an art project. She has 8 students and they will need 3 pieces of construction paper each. In addition to the construction paper, she needs to buy 6 bottles of glue for everyone to share. After Kelly purchases these supplies, she dropped half of them down a storm drain. Class is about to start, but she manages to rush to the store and buy 5 more pieces of construction paper. How many supplies are left?"""
    students = 8
    paper_per_student = 3
    total_paper = students * paper_per_student
    total_glue = 6
    half_supplies_lost = (total_paper + total_glue) / 2
    remaining_paper = (total_paper - half_supplies_lost) + 5
    remaining_glue = total_glue / 2
    result = remaining_paper + remaining_glue
    return result

print(solution())