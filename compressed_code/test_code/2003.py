def solution():
    
    single_yolk = 1
    double_yolk = 2
    eggs_per_carton = 12
    double_yolk_eggs = 5
    total_single_yolks = (eggs_per_carton - double_yolk_eggs) * single_yolk
    total_double_yolks = double_yolk_eggs * double_yolk
    total_yolks = total_single_yolks + total_double_yolks
    result = total_yolks
    return result

print(solution())