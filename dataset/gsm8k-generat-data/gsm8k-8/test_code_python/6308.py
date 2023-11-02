def solution():
    # Calculate the remaining amount to be paid
    remaining_payment = 13380 - 5400

    # Calculate the number of months needed to fully pay for the car
    months_to_pay = remaining_payment / 420

    # Round up the number of months to the nearest integer
    months_to_pay = math.ceil(months_to_pay)

    result = months_to_pay
    return result

print(solution())