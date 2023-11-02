def solution():
    
    single_carnation_price = 0.5
    dozen_price = 4
    num_teachers = 5
    num_friends = 14
    num_carnations = num_teachers * 12 + num_friends
    num_dozens = num_carnations // 12
    num_singles = num_carnations % 12
    total_price = num_dozens * dozen_price + num_singles * single_carnation_price
    result = total_price
    return result

print(solution())