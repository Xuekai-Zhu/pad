def solution():
    # Define the available submission methods and student ownership of fax machines
    submission_methods = ["email", "web portal", "paper", "fax"]
    student_owns_fax = False
    # Check if fax is a common submission method or if most students own fax machines
    if "fax" in submission_methods or student_owns_fax:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())