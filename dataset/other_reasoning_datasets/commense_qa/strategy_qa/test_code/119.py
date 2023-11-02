def solution():
    # Define that cancer is a diagnosis that can result in disability and that disability is determined by degree of impairment
    cancer_qualifies_for_disability = True
    disability_determined_by_impairment = True
    # Check if all cancer patients experience major impairment
    all_cancer_patients_experience_major_impairment = False
    if not all_cancer_patients_experience_major_impairment:
        result = "no"
    elif cancer_qualifies_for_disability and disability_determined_by_impairment:
        result = "yes"
    else:
        result = "unsure"
    return result

print(solution())