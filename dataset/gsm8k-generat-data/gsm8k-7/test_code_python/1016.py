def solution():
    total_fruit = 78

    # Calculate the number of kiwis in the crate
    num_kiwis = total_fruit / 3

    # Calculate the number of strawberries in the crate
    num_strawberries = total_fruit - num_kiwis
    result = num_strawberries
    return result

print(solution())