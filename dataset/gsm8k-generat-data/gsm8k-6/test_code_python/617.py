def solution():
    speed = 75  # miles per hour
    speed_limit = 30  # miles per hour
    fine_per_mph_over = 2  # dollars 
    base_fine = 50  # dollars
    double_fine = 2  # factor to double the fine for school zone
    court_costs = 300  # dollars
    lawyer_fee_per_hour = 80  # dollars
    hours_worked_by_lawyer = 3  # hours

    # Calculate the fine for speeding
    mph_over_limit = speed - speed_limit
    fine_for_speeding = base_fine + fine_per_mph_over * mph_over_limit

    # Double the fine for being in a school zone
    fine_with_school_zone = double_fine * fine_for_speeding

    # Calculate the total cost including court costs and lawyer fees
    total_cost = fine_with_school_zone + court_costs + lawyer_fee_per_hour * hours_worked_by_lawyer
    result = total_cost
    return result

print(solution())