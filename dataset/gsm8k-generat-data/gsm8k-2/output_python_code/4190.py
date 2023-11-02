def solution():
    """James has 20 years of experience.  8 years ago John had twice as much experience as James.  Mike started when John had 16 years of experience. What is their combined experience?"""
    james_exp = 20
    john_exp_8yo = (james_exp - 8) * 2
    john_exp = john_exp_8yo + 8
    mike_exp = john_exp - 16
    total_exp = james_exp + john_exp + mike_exp
    result = total_exp
    return result

print(solution())