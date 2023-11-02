def solution():
    """Dakota gets hit by a bus and has to spend 3 days in the hospital. The hospital charges her $900/day for her bed, $250/hour for two specialists to look at her 15 minutes each, and $1800 for the ambulance ride. How much is Dakota's medical bill?"""
    # Define the number of days in the hospital and the cost per day
    DAYS = 3
    BED_COST = 900

    # Define the cost of the ambulance ride
    AMBULANCE_COST = 1800

    # Define the cost per specialist per 15 minutes
    SPECIALIST_COST = 250 / 4

    # Calculate the total cost of the bed
    bed_total = DAYS * BED_COST

    # Calculate the total cost of the specialist consultations
    specialist_total = 2 * 2 * SPECIALIST_COST  # 2 specialists, 2 consultations each

    # Calculate the total medical bill
    medical_bill = bed_total + specialist_total + AMBULANCE_COST

    result = medical_bill
    return result

print(solution())