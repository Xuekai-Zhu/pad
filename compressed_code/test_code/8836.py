def solution():
    
    adults_per_hour = 4
    children_per_hour = 3
    adult_fee = 50
    child_fee = 25
    total_patients_per_hour = adults_per_hour + children_per_hour
    total_fee_per_hour = (adults_per_hour * adult_fee) + (children_per_hour * child_fee)
    total_fee_per_day = total_fee_per_hour * 8
    result = total_fee_per_day
    return result

print(solution())