def solution():
    """Dakota gets hit by a bus and has to spend 3 days in the hospital. The hospital charges her $900/day for her bed, $250/hour for two specialists to look at her 15 minutes each, and $1800 for the ambulance ride. How much is Dakota's medical bill?"""
    hospital_stay_days = 3
    bed_cost_per_day = 900
    specialist_cost_per_hour = 250
    specialist_time_in_minutes = 15
    ambulance_cost = 1800
    
    total_bed_cost = hospital_stay_days * bed_cost_per_day
    total_specialist_cost = 2 * specialist_cost_per_hour * (specialist_time_in_minutes/60) * 24 #total hours in 3 days
    total_medical_bill = total_bed_cost + total_specialist_cost + ambulance_cost
    
    result = total_medical_bill
    return result

print(solution())