def solution():
    # Calculate the total hours worked by the two men
    total_hours = 10 + 8 + 15

    # Calculate the total amount paid to each man for the total hours worked
    payment_per_man = total_hours * 10

    # Calculate the total amount paid to both men
    total_payment = payment_per_man * 2
    result = total_payment
    return result

print(solution())