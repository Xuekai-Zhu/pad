def solution():
    """Dorchester works at a puppy wash. He is paid $40 per day + $2.25 for each puppy he washes. On Wednesday, Dorchester earned $76. How many puppies did he wash that day?"""
    base_pay = 40
    pay_per_puppy = 2.25
    total_pay = 76
    puppies_washed = (total_pay - base_pay) / pay_per_puppy
    result = puppies_washed
    return result

print(solution())