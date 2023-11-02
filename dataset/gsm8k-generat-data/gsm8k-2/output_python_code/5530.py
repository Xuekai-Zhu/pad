def solution():
    """Dakota gets hit by a bus and has to spend 3 days in the hospital. The hospital charges her $900/day for her bed, $250/hour for two specialists to look at her 15 minutes each, and $1800 for the ambulance ride. How much is Dakota's medical bill?"""
    hospital_bed_cost = 900 * 3
    specialist_cost = (15/60) * 2 * 250 * 24 # 15 mins for each specialist, 2 specialists, 24 hours per day
    ambulance_cost = 1800
    total_cost = hospital_bed_cost + specialist_cost + ambulance_cost
    result = total_cost
    return result

print(solution())