def solution():
    # Convert farthings to pfennigs
    total_pfennigs = 54 / 6  # 6 farthings are equivalent to 1 pfennig
    
    # Subtract the cost of the meat pie from the total pfennigs
    remaining_pfennigs = total_pfennigs - 2
    
    result = remaining_pfennigs
    return result

print(solution())