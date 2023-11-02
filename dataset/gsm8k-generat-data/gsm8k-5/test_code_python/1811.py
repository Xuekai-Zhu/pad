def solution():
    students = 8  # Kelly has 8 students in her class
    paper_per_student = 3  # Each student needs 3 pieces of construction paper
    glue_bottles = 6  # Kelly needs to buy 6 bottles of glue for everyone to share

    # Calculate the total number of pieces of construction paper Kelly needs
    total_paper = students * paper_per_student

    # After losing half of the supplies, Kelly has half of the original amount left
    remaining_paper = int(0.5 * total_paper)
    remaining_glue = int(0.5 * glue_bottles)

    # Kelly buys 5 more pieces of construction paper
    remaining_paper += 5

    result = (remaining_paper, remaining_glue)
    return result

print(solution())