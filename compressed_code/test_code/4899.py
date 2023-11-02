def solution():
    
    total_veggies = 280
    tomato_ratio = 3
    total_ratio = 4
    cucumber_ratio = total_ratio - tomato_ratio
    total_parts = tomato_ratio + cucumber_ratio
    cucumber_count = (cucumber_ratio / total_parts) * total_veggies
    result = cucumber_count
    return result

print(solution())