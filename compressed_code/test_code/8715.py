def solution():
    
    num_of_girls = 5
    num_of_boys = 5
    avg_weight_girls = 45
    avg_weight_boys = 55
    total_weight = (num_of_girls * avg_weight_girls) + (num_of_boys * avg_weight_boys)
    avg_weight = total_weight / (num_of_girls + num_of_boys)
    result = avg_weight
    return result

print(solution())