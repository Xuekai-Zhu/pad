def solution():
    is_paresthesia_symptom_of_lead_poisoning = True
    is_lead_white_exposure_a_cause_of_lead_poisoning = True
    if is_paresthesia_symptom_of_lead_poisoning and is_lead_white_exposure_a_cause_of_lead_poisoning:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())