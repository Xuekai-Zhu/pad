def solution():
    initial_population = 300000
    immigration = 50000
    emigration = 30000
    total_population = initial_population + immigration - emigration
    pregnancy = total_population / 8
    twins = pregnancy / 4
    final_population = total_population + pregnancy + twins
    
    return final_population

print(solution())