def solution():
    base_pay = 40  # Dorchester's daily base pay
    total_pay = 76  # Dorchester's total pay for the day, including base pay and pay per puppy
    pay_per_puppy = 2.25  # Dorchester's pay per puppy washed

    # Calculate the number of puppies Dorchester washed
    puppies_washed = (total_pay - base_pay) / pay_per_puppy
    result = puppies_washed
    return result

print(solution())