def solution():
    # Define variables related to pancreas removal and bankruptcy
    is_medical_procedure = True
    is_expensive = True
    can_cause_debt = True
    can_cause_bankruptcy = True
    # Check if pancreas removal can cause bankruptcy
    if is_medical_procedure and is_expensive and can_cause_debt and can_cause_bankruptcy:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())