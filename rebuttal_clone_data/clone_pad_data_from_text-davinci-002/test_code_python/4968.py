def solution():
    carrots = 1
    broccoli = carrots * 2
    carrot_calories = 51
    broccoli_calories = carrot_calories / 3
    total_calories = carrot_calories * carrots + broccoli_calories * broccoli
    result = total_calories
    return result

print(solution())