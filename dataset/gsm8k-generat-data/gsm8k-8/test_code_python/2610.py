def solution():
    # Calculate the total number of eggs produced in 8 weeks
    total_eggs = 46 * 6 * 8

    # Calculate the number of dozens of eggs produced
    dozens_of_eggs = total_eggs / 12

    # Calculate the total amount of money earned
    total_money = dozens_of_eggs * 3

    result = total_money
    return result

print(solution())