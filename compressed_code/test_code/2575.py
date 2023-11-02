def solution():
    
    num_minor_characters = 4
    num_major_characters = 5
    minor_character_pay = 15000
    major_character_pay = 3 * minor_character_pay
    total_pay = (num_minor_characters * minor_character_pay) + (num_major_characters * major_character_pay)
    result = total_pay
    return result

print(solution())