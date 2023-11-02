def solution():
    """Jake's neighbors hire him to mow their lawn and plant some flowers. Mowing the lawn takes 1 hour and pays $15. If Jake wants to make $20/hour working for the neighbors, and planting the flowers takes 2 hours, how much should Jake charge (in total, not per hour) for planting the flowers?"""
    mowing_pay = 15
    desired_hourly_rate = 20
    planting_hours = 2
    total_planting_pay = planting_hours * desired_hourly_rate
    total_charge = total_planting_pay + mowing_pay
    result = total_charge
    return result

print(solution())