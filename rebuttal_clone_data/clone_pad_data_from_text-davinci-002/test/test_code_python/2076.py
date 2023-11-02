def solution():
    slice_1 = 4
    slice_2 = 7
    total_cost = slice_1 * 7 + slice_2 * 5
    money_paid = 100
    change_received = money_paid - total_cost
    result = change_received
    return result

print(solution())