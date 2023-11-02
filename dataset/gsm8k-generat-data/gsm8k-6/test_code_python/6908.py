def solution():
    # Calculate James' new lifting total and body weight
    new_total = 2200 * 1.15  
    new_weight = 245 + 8  

    # Calculate the ratio of lifting total to body weight
    ratio = new_total / new_weight  
    result = round(ratio, 2)
    return result

print(solution())