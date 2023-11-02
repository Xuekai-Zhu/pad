def solution():
    current_population = 4000
    new_population = current_population * 3
    growth_rate = 0.4
    years = 5

    # Calculate the future population of Mojave
    future_population = new_population * (1 + growth_rate) ** years
    result = future_population
    return result

print(solution())