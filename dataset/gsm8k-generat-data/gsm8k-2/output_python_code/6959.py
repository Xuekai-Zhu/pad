def solution():
    """Jake's neighbors hire him to mow their lawn and plant some flowers. Mowing the lawn takes 1 hour and pays $15. If Jake wants to make $20/hour working for the neighbors, and planting the flowers takes 2 hours, how much should Jake charge (in total, not per hour) for planting the flowers?"""
    lawn_pay = 15
    flower_hours = 2
    flower_hourly_rate = 20
    flower_pay = flower_hourly_rate * flower_hours
    total_pay = lawn_pay + flower_pay
    flower_charge = total_pay - lawn_pay

    result = flower_charge
    return result

print(solution())