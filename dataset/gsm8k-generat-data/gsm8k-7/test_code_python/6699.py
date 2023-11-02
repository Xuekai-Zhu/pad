def solution():
    num_bushes = 20
    bush_cost = 150
    gardener_hourly_rate = 30
    num_hours_per_day = 5
    num_days = 4
    soil_volume = 100
    soil_cost_per_cubic_foot = 5

    # Calculate the total cost of all rose bushes
    total_bush_cost = num_bushes * bush_cost

    # Calculate the total cost of the gardener's labor
    total_gardener_cost = gardener_hourly_rate * num_hours_per_day * num_days

    # Calculate the total cost of the soil
    total_soil_cost = soil_volume * soil_cost_per_cubic_foot

    # Calculate the total cost of the entire gardening project
    total_cost = total_bush_cost + total_gardener_cost + total_soil_cost
    result = total_cost
    return result

print(solution())