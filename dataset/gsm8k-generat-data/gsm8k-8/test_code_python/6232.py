def solution():
    # Calculate the number of girls at the party
    num_girls = 40/4

    # Calculate the amount each girl paid to attend the party
    girl_payment = 50/2

    # Calculate the total amount collected from the girls
    total_girl_payment = num_girls * girl_payment

    # Calculate the total amount collected from the boys
    total_boy_payment = 40 * 50

    # Calculate the total amount collected at the party
    total_payment = total_girl_payment + total_boy_payment

    result = total_payment
    return result

print(solution())