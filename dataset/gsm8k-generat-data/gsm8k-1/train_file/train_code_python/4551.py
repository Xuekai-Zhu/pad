def solution():
    """Millie, Monica, and Marius are taking subjects for school. Millie takes three more subjects than Marius, who takes 4 subjects more than Monica. If Monica took 10 subjects, how many subjects all take altogether?"""
    monica_subjects = 10
    marius_subjects = monica_subjects + 4
    millie_subjects = marius_subjects + 3
    total_subjects = monica_subjects + marius_subjects + millie_subjects
    result = total_subjects
    return result

print(solution())