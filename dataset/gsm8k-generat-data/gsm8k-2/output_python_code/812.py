def solution():
    """Tom cannot afford a normal doctor, so he goes to a discount clinic that is 70% cheaper. It takes two visits, though, instead of 1. A normal doctor charges $200 for a visit. How much money does he save?"""
    normal_doctor_charge = 200
    discount_rate = 0.7
    discount_doctor_charge = normal_doctor_charge - (normal_doctor_charge * discount_rate)
    total_visits = 2
    normal_doctor_total_cost = normal_doctor_charge * total_visits
    discount_doctor_total_cost = discount_doctor_charge * total_visits
    total_savings = normal_doctor_total_cost - discount_doctor_total_cost
    result = total_savings
    return result

print(solution())