def solution():
    initial_lions = 100
    births_per_month = 5
    deaths_per_month = 1
    months_per_year = 12

    # Calculate the net change in the lion population per month
    net_change_per_month = births_per_month - deaths_per_month

    # Calculate the total net change in the lion population after one year
    total_net_change = net_change_per_month * months_per_year

    # Calculate the new lion population after one year
    lion_population = initial_lions + total_net_change
    result = lion_population
    return result

print(solution())