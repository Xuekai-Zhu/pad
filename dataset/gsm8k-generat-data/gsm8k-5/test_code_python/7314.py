def solution():
    fries_per_potato = 25  # The chef can get 25 fries out of 1 potato
    total_fries_needed = 200  # The chef needs to make 200 fries
    potatoes_needed = total_fries_needed / fries_per_potato  # The number of potatoes needed
    potatoes_leftover = 15 - potatoes_needed  # The number of potatoes leftover

    result = potatoes_leftover
    return result

print(solution())