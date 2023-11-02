def solution():
    
    nicole_clothes = 10
    first_sister_clothes = nicole_clothes / 2
    second_sister_clothes = nicole_clothes + 2
    oldest_sister_clothes = (nicole_clothes + first_sister_clothes + second_sister_clothes) / 3
    total_clothes = nicole_clothes + first_sister_clothes + second_sister_clothes + oldest_sister_clothes
    result = total_clothes
    return result

print(solution())