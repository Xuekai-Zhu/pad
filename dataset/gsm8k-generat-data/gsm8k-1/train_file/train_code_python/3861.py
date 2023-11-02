def solution():
    """When Doctor Lindsay works in her office, she usually sees 4 adult patients and 3 child patients every hour. If the cost for an adult's office visit is $50, and the cost for a child's office visit is $25, how much money, in dollars, does Doctor Lyndsay receive in a typical 8-hour day for seeing all her patients?"""
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