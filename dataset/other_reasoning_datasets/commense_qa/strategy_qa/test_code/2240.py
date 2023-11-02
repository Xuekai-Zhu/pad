def solution():
    # Define the physical and behavioral symptoms of stroke
    physical_symptoms = ["facial unevenness", "trouble walking"]
    behavioral_symptoms = ["slurred speech", "disorientation", "trouble understanding speech"]
    # Check if there are any symptoms present
    if physical_symptoms or behavioral_symptoms:
        result = "no, it is possible to tell if someone is having a stroke"
    else:
        result = "yes, it may be impossible to tell if someone is having a stroke without a medical examination"
    return result

print(solution())