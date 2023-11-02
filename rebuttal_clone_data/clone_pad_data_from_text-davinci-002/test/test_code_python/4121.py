def solution():
    jars = 4
    cucumbers = 10
    vinegar = 100
    pickles_per_cucumber = 6
    pickles_per_jar = 12
    vinegar_per_jar = 10
    
    total_pickles = jars * pickles_per_jar
    total_cucumbers = cucumbers * pickles_per_cucumber
    total_vinegar = vinegar_per_jar * jars
    
    leftover_vinegar = vinegar - total_vinegar
    
    if total_cucumbers > total_pickles:
        result = leftover_vinegar
    else:
        result = 0
    
    return result

print(solution())