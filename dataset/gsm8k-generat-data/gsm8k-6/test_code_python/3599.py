def solution():
    # Calculate the total number of shrimp caught by the three boys
    shrimp_Austin = 26 - 8  # Austin's trap caught 8 less than Victor's
    shrimp_total = 26 + shrimp_Austin + (1/2) * (26 + shrimp_Austin)  # Brian's trap caught half of Victor and Austin's total number of shrimp
    
    # Calculate the total earnings from selling the shrimp
    earnings_total = (7/11) * shrimp_total
    
    # Calculate how much each boy will earn
    earnings_per_boy = earnings_total / 3
    
    result = earnings_per_boy
    return result

print(solution())