def solution():
    # Calculate total number of windows in the house
    total_windows = 3 * 3 * 3

    # Calculate the amount Lucas will be paid without any deductions
    payment_no_deductions = total_windows * 2

    # Calculate the number of 3-day periods that have passed
    num_periods = 6 // 3

    # Calculate the deduction for incomplete work
    deduction = num_periods * 1

    # Calculate Lucas' total payment after deductions
    total_payment = payment_no_deductions - deduction
    result = total_payment
    return result

print(solution())