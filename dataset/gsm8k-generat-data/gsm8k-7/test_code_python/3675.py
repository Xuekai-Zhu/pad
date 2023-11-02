def solution():
    borrowing_amount = 100
    num_weeks = 2
    initial_fee_rate = 0.05

    # Calculate the total finance fee
    total_fee = 0
    current_fee_rate = initial_fee_rate
    for i in range(num_weeks):
        current_fee = borrowing_amount * current_fee_rate
        total_fee += current_fee
        current_fee_rate *= 2

    result = total_fee
    return result

print(solution())