def solution():
    daily_pay = 40
    per_puppy_pay = 2.25
    total_pay = 76
    number_of_puppies = (total_pay - daily_pay) / per_puppy_pay
    result = number_of_puppies
    return result

print(solution())