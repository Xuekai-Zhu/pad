def solution():
    initial_ants = 100  # Number of ants in the first anthill
    decrease_rate = 0.2  # 20% decrease in ants in each successive anthill

    # Calculate the number of ants in each successive anthill
    ants_2 = initial_ants * (1 - decrease_rate)
    ants_3 = ants_2 * (1 - decrease_rate)

    # Round ants in the third anthill to the nearest whole number
    ants_3 = round(ants_3)

    result = ants_3
    return result

print(solution())