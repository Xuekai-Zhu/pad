def solution():
    mowing_pay = 15
    mowing_time = 1
    desired_hourly_rate = 20
    flower_planting_time = 2

    # Calculate how much Jake earns per hour mowing the lawn
    mowing_hourly_rate = mowing_pay / mowing_time

    # Calculate how much Jake should charge per hour for planting flowers
    flower_hourly_rate = desired_hourly_rate - mowing_hourly_rate

    # Calculate how much Jake should charge for the 2 hours of flower planting
    flower_charges = flower_hourly_rate * flower_planting_time

    result = flower_charges
    return result

print(solution())