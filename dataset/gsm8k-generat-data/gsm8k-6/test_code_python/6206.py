def solution():
    # Calculate the total cost of the items
    total_cost = 140 + 100 + 20  # computer table costs $140, computer chair costs $100, joystick costs $20

    # Calculate the amount Frank pays for the joystick
    frank_joystick_payment = 1/4 * 20  # Frank pays 1/4 of the joystick price

    # Calculate the total amount paid by Frank
    frank_total_payment = 140 + frank_joystick_payment  # Frank pays for the computer table and his share of the joystick

    # Calculate the amount paid by Eman
    eman_payment = total_cost - frank_total_payment  # Eman pays for the computer chair and her share of the joystick

    # Calculate the difference between Frank's and Eman's total payment
    difference = frank_total_payment - eman_payment
    result = difference
    return result

print(solution())