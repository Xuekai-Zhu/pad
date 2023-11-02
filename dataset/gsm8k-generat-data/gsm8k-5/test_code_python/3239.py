def solution():
    property_damage = 40000  # Property damage costs $40,000
    medical_bills = 70000  # Medical bills cost $70,000
    insurance_coverage = 0.8  # Carl's insurance company will cover 80% of the costs

    # Calculate the amount of the costs that Carl will have to pay personally
    personal_cost = (1 - insurance_coverage) * (property_damage + medical_bills)
    result = personal_cost
    return result

print(solution())