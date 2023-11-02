def solution():
    # Calculate the total value of Marly's bills
    total_value = 10 * 20 + 8 * 10 + 4 * 5

    # Calculate the number of $100 bills Marly will have after changing her bills
    num_hundreds = total_value // 100

    result = num_hundreds
    return result

print(solution())