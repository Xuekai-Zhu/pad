def solution():
    # Calculate the number of computers John was able to fix right away
    unfixable = 0.2 * 20  # 20% of the computers were unfixable
    need_spare_parts = 0.4 * 20  # 40% of the computers needed spare parts
    fixed_right_away = 20 - unfixable - need_spare_parts  # the remaining computers can be fixed right away
    result = fixed_right_away
    return result

print(solution())