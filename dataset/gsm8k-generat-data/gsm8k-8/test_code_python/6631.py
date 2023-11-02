def solution():
    # Calculate the number of people in the bottom 20%
    bottom_20_percent = int(0.2 * 1000)

    # Calculate the cost of the stimulus
    stimulus_cost = bottom_20_percent * 2000

    # Calculate the revenue generated from the stimulus
    revenue_generated = stimulus_cost * 5

    # Calculate the government's profit from the project
    profit = revenue_generated - stimulus_cost
    result = profit
    return result

print(solution())