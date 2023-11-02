def solution():
    # Calculate the cost for the hospital bed
    bed_cost = 900 * 3

    # Calculate the cost for the specialist consultations
    specialist_cost = 2 * (250 * 0.25 * 4)  # 4 consultations x 15 minutes x $250/hour

    # Calculate the cost for the ambulance ride
    ambulance_cost = 1800

    # Calculate the total medical bill
    total_cost = bed_cost + specialist_cost + ambulance_cost
    result = total_cost
    return result

print(solution())