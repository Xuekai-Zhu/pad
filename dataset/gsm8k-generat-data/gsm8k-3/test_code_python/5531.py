def solution():
    """Dakota gets hit by a bus and has to spend 3 days in the hospital. The hospital charges her $900/day for her bed, $250/hour for two specialists to look at her 15 minutes each, and $1800 for the ambulance ride. How much is Dakota's medical bill?"""
    # Define the cost for each service
    BED_COST_PER_DAY = 900
    SPECIALIST_COST_PER_HOUR = 250 * 2 * 4 # Two specialists, each spending 15 minutes => 0.5 hour per specialist, 1 hour total => 250 * 2 * 4 = 2000
    AMBULANCE_RIDE_COST = 1800

    # Calculate the total cost for Dakota's hospital stay
    days_in_hospital = 3
    bed_cost = BED_COST_PER_DAY * days_in_hospital
    specialist_cost = SPECIALIST_COST_PER_HOUR
    total_cost = bed_cost + specialist_cost + AMBULANCE_RIDE_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())