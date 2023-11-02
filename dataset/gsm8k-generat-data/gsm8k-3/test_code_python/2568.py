def solution():
    """A local farm is famous for having lots of double yolks in their eggs. One carton of 12 eggs had five eggs with double yolks. How many yolks were in the whole carton?"""
    # Define the number of eggs in a carton and the number of double yolk eggs
    CARTON_SIZE = 12
    DOUBLE_YOLK_EGGS = 5

    # Calculate the total number of yolks in the carton
    total_yolks = CARTON_SIZE * 2 - DOUBLE_YOLK_EGGS

    # Display the total number of yolks
    result = total_yolks
    return result

print(solution())