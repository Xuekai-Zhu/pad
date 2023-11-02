def solution():
    # Calculate the total weight of all the men
    total_men_weight = 8 * 190  

    # Calculate the total weight of all the women
    total_women_weight = 6 * 120
    
    # Calculate the total weight of all the men and women
    total_weight = total_men_weight + total_women_weight
    
    # Calculate the average weight of all the men and women
    avg_weight = total_weight / 14
    
    result = avg_weight
    return result

print(solution())