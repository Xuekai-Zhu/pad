def solution():
    
    total_gallons = 4.5
    total_pints = total_gallons * 8
    thermoses = 18
    genevieve_thermoses = 3
    genevieve_pints = (total_pints / thermoses) * genevieve_thermoses
    result = genevieve_pints
    return result

print(solution())