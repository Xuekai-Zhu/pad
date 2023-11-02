def solution():
    # Calculate the total number of yolks in the carton
    double_yolk_eggs = 5  # number of eggs with double yolks
    single_yolk_eggs = 12 - double_yolk_eggs  # number of eggs with single yolks
    total_yolks = (2 * double_yolk_eggs) + single_yolk_eggs  # total yolks in the carton (double yolks count as two)
    result = total_yolks
    return result

print(solution())