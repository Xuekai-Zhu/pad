def solution():
    
    eggs_per_carton = 12
    double_yolk_eggs = 5
    single_yolk_eggs = eggs_per_carton - double_yolk_eggs
    total_yolks = (double_yolk_eggs * 2) + single_yolk_eggs
    result = total_yolks
    return result

print(solution())