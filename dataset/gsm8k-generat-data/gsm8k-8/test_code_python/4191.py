def solution():
    james_exp = 20
    john_exp_8yrs_ago = 2 * (james_exp - 8)
    john_exp = john_exp_8yrs_ago + 8
    mike_exp = john_exp - 16
    combined_exp = james_exp + john_exp + mike_exp
    result = combined_exp
    return result

print(solution())