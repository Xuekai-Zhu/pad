def solution():
    
    standard_fee = 80
    veteran_fee = standard_fee * 0.25
    num_standard_lessons = 4
    num_veteran_lessons = 2
    total_standard_fee = standard_fee * num_standard_lessons
    total_veteran_fee = veteran_fee * num_veteran_lessons
    total_fee = total_standard_fee + total_veteran_fee
    result = total_fee
    return result

print(solution())