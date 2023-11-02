def solution():
    """A local farm is famous for having lots of double yolks in their eggs. One carton of 12 eggs had five eggs with double yolks. How many yolks were in the whole carton?"""
    eggs_per_carton = 12
    double_yolk_eggs = 5
    single_yolk_eggs = eggs_per_carton - double_yolk_eggs
    total_yolks = (double_yolk_eggs * 2) + single_yolk_eggs
    result = total_yolks
    return result

print(solution())