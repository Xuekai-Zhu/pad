def solution():
    field_of_study = "Biochemistry"
    topic_of_interest = "biomolecules"
    involves_atoms = True
    if topic_of_interest in field_of_study and not involves_gluons:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())