def solution():
    james_exp = 20  # James has 20 years of experience
    john_exp_8_years_ago = james_exp - 8 * 2  # 8 years ago, John had twice as much experience as James
    john_exp = john_exp_8_years_ago + 8  # John's current experience
    mike_exp = john_exp - 16  # Mike started when John had 16 years of experience

    # Calculate the total combined experience
    total_exp = james_exp + john_exp + mike_exp
    result = total_exp
    return result

print(solution())