def solution():
    """Millie, Monica, and Marius are taking subjects for school. Millie takes three more subjects than Marius, who takes 4 subjects more than Monica. If Monica took 10 subjects, how many subjects all take altogether?"""
    # Define the number of subjects Monica is taking
    monica_subjects = 10

    # Calculate the number of subjects Marius is taking
    marius_subjects = monica_subjects + 4

    # Calculate the number of subjects Millie is taking
    millie_subjects = marius_subjects + 3

    # Calculate the total number of subjects taken by all three
    total_subjects = monica_subjects + marius_subjects + millie_subjects

    # Display the total number of subjects
    result = total_subjects
    return result

print(solution())