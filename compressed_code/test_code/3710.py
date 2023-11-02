def solution():
    
    growth_rates = [1, 2, 2, 3]  
    total_growth = 0

    for i in range(4):
        if i == 1:
            growth_rates[i] = growth_rates[0] * 2
        if i == 3:
            growth_rates[i] = growth_rates[2] + 1

        total_growth += growth_rates[i] * 4

    result = total_growth
    return result

print(solution())