def solution():
    depression_symptoms = ["low energy", "inability to get out of bed", "low motivation"]
    possible_mistaken_symptoms = ["low energy", "low motivation"]
    if all(symptom in depression_symptoms for symptom in possible_mistaken_symptoms):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())