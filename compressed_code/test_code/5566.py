def solution():
    
    base_pay = 40
    pay_per_puppy = 2.25
    total_pay = 76
    puppies_washed = (total_pay - base_pay) / pay_per_puppy
    result = puppies_washed
    return result

print(solution())