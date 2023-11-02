def solution():
    
    total_apples = 80
    ali_ratio = 4
    sara_ratio = 1
    total_ratio = ali_ratio + sara_ratio
    sara_apples = (sara_ratio/total_ratio)*total_apples
    result = sara_apples
    return result

print(solution())