def solution():
    """Millie, Monica, and Marius are taking subjects for school. Millie takes three more subjects than Marius, who takes 4 subjects more than Monica. If Monica took 10 subjects, how many subjects all take altogether?"""
    # Define the initial number of subjects taken by Monica
    monica_subjects = 10

    # Calculate the number of subjects taken by Marius
    marius_subjects = monica_subjects + 4

    # Calculate the number of subjects taken by Millie
    millie_subjects = marius_subjects + 3

    # Calculate the total number of subjects taken by all three students
    total_subjects = monica_subjects + marius_subjects + millie_subjects

    # return the result
    result = total_subjects
    return result

print(solution())