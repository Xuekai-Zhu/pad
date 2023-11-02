def solution():
    # Define the base pay and total pay for Wednesday
    base_pay = 40
    total_pay = 76

    # Calculate the amount Dorchester earned from washing puppies
    puppy_pay = total_pay - base_pay

    # Calculate the number of puppies Dorchester washed
    num_puppies = int(puppy_pay / 2.25)
    result = num_puppies
    return result

print(solution())