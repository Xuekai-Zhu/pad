def solution():
    num_eggs = 12
    num_double_yolks = 5
    yolks_per_egg = 2

    # Calculate the total number of yolks in the carton
    total_yolks = (num_eggs * yolks_per_egg) - (num_double_yolks * (yolks_per_egg - 1))
    result = total_yolks
    return result

print(solution())