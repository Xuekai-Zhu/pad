def solution():
    pregnancy_symptoms = ["nausea", "stomach upset"]
    ginger_dosage = "small"
    ginger_safe = True
    if any(symptom in pregnancy_symptoms for symptom in ["nausea", "vomiting"]) and ginger_safe and ginger_dosage == "small":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())