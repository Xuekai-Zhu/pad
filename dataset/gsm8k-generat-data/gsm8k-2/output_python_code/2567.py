def solution():
    """A local farm is famous for having lots of double yolks in their eggs. One carton of 12 eggs had five eggs with double yolks. How many yolks were in the whole carton?"""
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