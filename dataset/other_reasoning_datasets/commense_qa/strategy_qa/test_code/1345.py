def solution():
    derogatory_terms = ["ape", "monkey"]
    is_abusive = True
    is_teacher = True
    is_black_student = True
    # Check if the situation violates the teacher's code of conduct
    if is_teacher and is_black_student and is_abusive and any(term in derogatory_terms for term in text.lower().split()):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())