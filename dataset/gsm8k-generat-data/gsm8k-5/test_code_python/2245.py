def solution():
    initial_lions = 100  # There are 100 lions at first
    cubs_born_per_month = 5  # 5 lion cubs are born per month
    lions_die_per_month = 1  # 1 lion dies per month
    months_in_year = 12  # There are 12 months in a year

    # Calculate the net change in the lion population per month
    net_change_per_month = cubs_born_per_month - lions_die_per_month

    # Calculate the total change in the lion population after 1 year
    total_population_change = net_change_per_month * months_in_year

    # Calculate the final lion population after 1 year
    final_lion_population = initial_lions + total_population_change
    result = final_lion_population
    return result

print(solution())