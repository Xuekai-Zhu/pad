def solution():
    hospital_bed_cost = 900 * 3  # Dakota spent 3 days in the hospital and each day cost $900 for the bed
    specialist_cost = 250 * 0.5 * 2  # Two specialists looked at Dakota for 15 minutes each, which is 0.5 hours in total, at a cost of $250/hour each
    ambulance_ride_cost = 1800  # Dakota's ambulance ride cost $1800
    total_cost = hospital_bed_cost + specialist_cost + ambulance_ride_cost
    result = total_cost
    return result

print(solution())