def solution():
    is_Rand_Paul_an_ophthalmologist_with_approved_certification_in_NY = False
    is_certification_required_in_Kentucky = False
    is_NY_approval_required = True
    if not is_Rand_Paul_an_ophthalmologist_with_approved_certification_in_NY and (not is_certification_required_in_Kentucky or is_NY_approval_required):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())