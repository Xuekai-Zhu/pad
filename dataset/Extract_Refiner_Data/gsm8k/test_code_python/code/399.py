def solution():
    
    # Define the initial energy usage and the reduction hours per day
    initial_energy_usage = 900
    reduction_hours = 5

    # Calculate the energy usage per day
    daily_energy_usage = initial_energy_usage / reduction_hours

    # Calculate the energy savings per day
    energy_savings_per_day = daily_energy_usage * 1000

    # Calculate the energy savings in 30 days
    energy_savings_in_30_days = energy_savings_per_day * 30

    # return the result
    result = energy_savings_in_30_days
    return result

print(solution())