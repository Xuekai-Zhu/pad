def solution():
    # Calculate the total number of sacks of rice after the first harvest
    first_harvest = 20  # initial yield is 20 sacks
    increased_yield = first_harvest * 0.2  # 20 percent increase in yield
    total_yield_first_harvest = first_harvest + increased_yield
    # Calculate the total number of sacks of rice after the second harvest
    second_harvest = total_yield_first_harvest
    increased_yield = second_harvest * 0.2
    total_yield_second_harvest = second_harvest + increased_yield
    result = total_yield_first_harvest + total_yield_second_harvest
    return result

print(solution())