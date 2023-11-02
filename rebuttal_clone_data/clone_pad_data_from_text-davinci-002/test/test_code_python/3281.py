def solution():
    total_flowers = 40
    roses = total_flowers * 2/5
    tulips = 10
    carnations = total_flowers - roses - tulips
    result = carnations
    
    return result

print(solution())