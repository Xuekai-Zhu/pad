def solution():
    eggs_per_carton = 12  # There are 12 eggs in a carton
    eggs_with_double_yolks = 5  # There are 5 eggs with double yolks in a carton

    # Calculate the total number of yolks in the carton
    total_yolks = (eggs_per_carton - eggs_with_double_yolks) + (eggs_with_double_yolks * 2)

    result = total_yolks
    return result

print(solution())