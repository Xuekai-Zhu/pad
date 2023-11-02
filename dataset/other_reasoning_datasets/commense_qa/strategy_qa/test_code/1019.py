def solution():
    profession = "Accounting"
    learning_disability = "Dyscalculia"
    common_symptoms = ["difficulty with number sense", "difficulty with fact and calculation"]
    if learning_disability in profession and any(symptom in common_symptoms for symptom in profession):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())