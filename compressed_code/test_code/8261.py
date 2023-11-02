def solution():
    
    nicole_clothes = 10
    sister1_clothes = nicole_clothes / 2
    sister2_clothes = nicole_clothes + 2
    sister3_clothes = (nicole_clothes + sister1_clothes + sister2_clothes) / 3
    total_clothes = nicole_clothes + sister1_clothes + sister2_clothes + sister3_clothes
    result = total_clothes
    return result

print(solution())