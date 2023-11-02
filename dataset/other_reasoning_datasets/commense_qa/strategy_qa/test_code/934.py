def solution():
    prozac_treatment_type = "antidepressant"
    great_depression_type = "economic phenomenon"
    if prozac_treatment_type == "antidepressant" and great_depression_type != "psychological disorder":
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())