def solution():
    bill_total = 5000  # Josephine's hospital bill is $5000
    medication_cost = 0.5 * bill_total  # 50% of the bill is for medication
    remaining_bill = bill_total - medication_cost  # Subtract medication cost from total bill
    overnight_stay_cost = 0.25 * remaining_bill  # 25% of the remaining bill is for overnight stays
    food_cost = 175  # $175 is for food
    ambulance_cost = bill_total - medication_cost - overnight_stay_cost - food_cost  # Subtract all other costs from total bill to get ambulance cost

    result = ambulance_cost
    return result

print(solution())