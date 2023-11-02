def solution():
    """A local farm is famous for having lots of double yolks in their eggs. One carton of 12 eggs had five eggs with double yolks. How many yolks were in the whole carton?"""
    # Define the number of eggs in the carton
    eggs_in_carton = 12

    # Define the number of eggs with double yolks
    double_yolk_eggs = 5

    # Calculate the total number of yolks in the carton
    total_yolks = (eggs_in_carton * 2) - double_yolk_eggs

    # return the result
    result = total_yolks
    return result

print(solution())