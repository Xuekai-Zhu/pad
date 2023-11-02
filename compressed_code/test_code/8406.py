def solution():
    
    main_characters = 5
    minor_characters = 4
    minor_pay = 15000
    major_pay = minor_pay * 3
    total_pay = (main_characters * major_pay) + (minor_characters * minor_pay)
    result = total_pay
    return result

print(solution())