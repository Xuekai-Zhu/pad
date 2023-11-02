def solution():
    ada_compliant = False
    wheelchair_accessible = False
    # Check if the business is ADA compliant
    if not ada_compliant:
        # Check if the business has wheelchair access points
        if not wheelchair_accessible:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())