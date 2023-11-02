def solution():
    has_clinical_evidence = True
    has_scientific_basis = True
    if not has_clinical_evidence or not has_scientific_basis:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())