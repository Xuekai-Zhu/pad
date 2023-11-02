def solution():
    # Calculate the interest on the first bill
    interest1 = 200 * 0.1 * 2

    # Calculate the late fees on the second bill
    late_fee2 = 50 * 6

    # Calculate the late fees on the third bill
    late_fee3 = 40 + 2*40

    # Calculate the total amount due for all three bills
    total_due = 200 + interest1 + 130 + late_fee2 + 444 + late_fee3

    result = total_due
    return result

print(solution())