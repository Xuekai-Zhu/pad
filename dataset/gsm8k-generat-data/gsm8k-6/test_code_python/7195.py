def solution():
    # Calculate the number of puppies Dorchester washed on Wednesday
    base_pay = 40  # Dorchester's base pay
    total_pay = 76  # Dorchester's total pay on Wednesday
    puppy_pay = total_pay - base_pay  # Dorchester's pay for washing puppies
    puppies_washed = puppy_pay / 2.25  # Dorchester is paid $2.25 for each puppy he washes
    result = puppies_washed
    return result

print(solution())