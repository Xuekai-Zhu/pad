def solution():
    # Find the number of subjects Marius takes
    marius_subjects = 10 + 4  

    # Find the number of subjects Millie takes
    millie_subjects = marius_subjects + 3  

    # Find the total number of subjects they take altogether
    total_subjects = monica_subjects + marius_subjects + millie_subjects
    result = total_subjects
    return result

print(solution())