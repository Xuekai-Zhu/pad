def solution():
    base_fine = 50
    speed = 75
    speed_limit = 30
    fine_per_mph_over_limit = 2
    fine_in_school_zone = 2
    court_cost = 300
    lawyer_fee_per_hour = 80
    hours_worked_by_lawyer = 3

    # Calculate the fine for speeding, including additional penalties
    fine_for_speeding = base_fine + fine_per_mph_over_limit * (speed - speed_limit)

    # Double the fine for being in a school zone
    total_fine = fine_for_speeding * fine_in_school_zone

    # Add court costs and lawyer fees
    total_fine += court_cost + lawyer_fee_per_hour * hours_worked_by_lawyer

    result = total_fine
    return result

print(solution())