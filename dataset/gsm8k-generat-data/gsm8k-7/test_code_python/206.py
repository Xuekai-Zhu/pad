def solution():
    lion_birth_rate = 5
    lion_death_rate = 1
    lions_after_year = 148
    months_in_year = 12

    # Calculate the net change in lion population per month
    net_lion_change = lion_birth_rate - lion_death_rate

    # Calculate the total net change in lion population after a year
    total_lion_change = net_lion_change * months_in_year

    # Calculate the initial number of lions in Londolozi
    initial_lion_population = lions_after_year - total_lion_change
    result = initial_lion_population
    return result

print(solution())