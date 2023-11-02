def solution():
    # Calculate the cost of a visit to a normal doctor
    normal_doctor_visit_cost = 200

    # Calculate the cost of a visit to the discount clinic
    discount_clinic_visit_cost = normal_doctor_visit_cost * 0.3

    # Calculate the total cost for two visits to the discount clinic
    total_discount_clinic_cost = 2 * discount_clinic_visit_cost

    # Calculate the amount of money saved
    money_saved = 2 * normal_doctor_visit_cost - total_discount_clinic_cost
    result = money_saved
    return result

print(solution())