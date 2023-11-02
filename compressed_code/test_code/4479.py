def solution():
    
    total_flowers = 40
    roses = (2/5) * total_flowers
    tulips = 10
    carnations = total_flowers - roses - tulips
    result = carnations
    return result

print(solution())