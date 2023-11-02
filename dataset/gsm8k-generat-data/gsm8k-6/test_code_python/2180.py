def solution():
    # Calculate the amount each friend has to pay initially
    initial_payment = 1700 / 6  # cost of the car is $1700 and there are 6 friends

    # Calculate the total amount they raised after the car wash
    total_raised = initial_payment * 6 - 500  # each friend paid initial_payment, there were 6 friends and they raised $500 at the car wash

    # Calculate the new amount each friend has to pay without Brad
    new_payment = total_raised / 5  # there are now only 5 friends participating in the car purchase

    # Calculate the difference in payment for each friend now that Brad isn't participating
    difference = new_payment - initial_payment

    result = difference
    return result

print(solution())