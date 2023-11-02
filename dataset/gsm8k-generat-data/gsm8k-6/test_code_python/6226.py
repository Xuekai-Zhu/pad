def solution():
    # Calculate the total number of eggs used to make all the omelettes
    eggs_for_3_omelettes = 3 * (5 + 3)  # 5 customers order 3 egg omelettes in the first hour, and 3 customers order them in the third hour
    eggs_for_4_omelettes = 4 * (7 + 8)  # 7 customers order 4 egg omelettes in the second hour, and 8 customers order them in the last hour
    total_eggs = eggs_for_3_omelettes + eggs_for_4_omelettes
    result = total_eggs
    return result

print(solution())