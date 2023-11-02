def solution():
    # Calculate the total energy consumed by the electric fan per day
    energy_per_day = (75/1000) * 8  # converting watts to kWh

    # Calculate the total energy consumed by the electric fan per month
    energy_per_month = energy_per_day * 30

    result = energy_per_month
    return result

print(solution())