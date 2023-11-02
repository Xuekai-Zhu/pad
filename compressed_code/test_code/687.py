def solution():
    
    first_half_hours = 12
    second_half_hours = 14
    first_half_money = first_half_hours * 5000
    second_half_money = second_half_hours * 5000 * 1.2
    total_money = first_half_money + second_half_money
    result = total_money
    return result

print(solution())