def solution():
    has_herpes = True
    bound_by_HIPAA = True
    if has_herpes and bound_by_HIPAA:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())