def solution():
    # Define whether eating undercooked meat causes food poisoning and whether elevated core body temperature is a symptom
    undercooked_meat_causes_food_poisoning = True
    elevated_body_temp_is_a_symptom = True
    # Check if eating undercooked meat can cause a fever
    if undercooked_meat_causes_food_poisoning and elevated_body_temp_is_a_symptom:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())