def solution():
    
    price_per_square_foot = 0.1
    book_set_cost = 150
    total_area_mowed = (20*15)*3
    money_earned = price_per_square_foot * total_area_mowed
    remaining_area = (book_set_cost - money_earned) / price_per_square_foot
    result = remaining_area
    return result

print(solution())