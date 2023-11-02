def solution():
    """If Ruby is 2 centimeters shorter than Pablo. Pablo is 70 centimeters taller than Charlene. Janet is 62 centimeters tall and Charlene is twice that tall. How tall is Ruby?"""
    charlene_height = 62
    pablo_height = charlene_height + 70
    ruby_height = pablo_height - 2
    result = ruby_height
    return result

print(solution())