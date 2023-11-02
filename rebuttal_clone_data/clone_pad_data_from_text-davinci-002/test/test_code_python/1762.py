def solution():
    nicole_clothes = 10
    first_sister = nicole_clothes / 2
    second_sister = nicole_clothes + 2
    third_sister = (first_sister + nicole_clothes + second_sister) / 3
    total_clothes = nicole_clothes + first_sister + second_sister + third_sister
    result = total_clothes
    return result

print(solution())