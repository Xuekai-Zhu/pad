def solution():
    tuition_fee = 90
    part_time_pay = 15 * 3
    scholarship = tuition_fee * 0.3

    total_paid = part_time_pay + scholarship
    still_needed = tuition_fee - total_paid
    result = still_needed
    return result

print(solution())