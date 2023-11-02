def solution():
    
    james_exp = 20
    john_exp_8_years_ago = (james_exp - 8) * 2
    john_exp = john_exp_8_years_ago + 8
    mike_exp = john_exp - 16
    combined_exp = james_exp + john_exp + mike_exp
    result = combined_exp
    return result

print(solution())