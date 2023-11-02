def solution():
    
    tuition_fee = 90
    part_time_pay = 15
    scholarship_percent = 0.3
    scholarship_amount = tuition_fee * scholarship_percent
    remaining_tuition_fee = tuition_fee - scholarship_amount
    remaining_tuition_fee -= part_time_pay * 3
    result = remaining_tuition_fee
    return result

print(solution())