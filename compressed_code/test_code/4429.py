def solution():
    
    capacity = 2000
    total_people = 0.75 * capacity
    full_fee = capacity * 20
    partial_fee = total_people * 20
    difference = full_fee - partial_fee
    result = difference
    return result

print(solution())