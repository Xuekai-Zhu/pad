def solution():
    total_peppers = 7 + 12 + 14 + 12 + 5 + 18 + 12
    hot_peppers = total_peppers * 0.20
    non_hot_peppers = total_peppers - hot_peppers
    result = non_hot_peppers
    
    return result

print(solution())