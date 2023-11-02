def solution():
    computer_table_cost = 140
    computer_chair_cost = 100
    joystick_cost = 20

    # Frank pays for the computer table
    frank_payment = computer_table_cost

    # Eman pays for the computer chair and part of the joystick
    eman_payment = computer_chair_cost + (3/4) * joystick_cost

    # Calculate the difference in payments
    difference = frank_payment - eman_payment
    result = difference
    return result

print(solution())