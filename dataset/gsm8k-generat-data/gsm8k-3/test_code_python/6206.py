def solution():
    """Two siblings, Eman and Frank, agreed to buy a new computer table, computer chair, and a joystick. The computer table costs $140, the computer chair costs $100, and the joystick costs $20. Eman agreed to pay for the computer chair while Frank agreed to pay for the computer table. Then Frank agreed to pay 1/4 of the price of the joystick and the rest will be paid by Eman. How much more money will Frank spend than Eman?"""
    # Define the prices of the items
    TABLE_PRICE = 140
    CHAIR_PRICE = 100
    JOYSTICK_PRICE = 20

    # Frank pays for the table
    frank_payment = TABLE_PRICE

    # Eman pays for the chair and 3/4 of the joystick
    eman_payment = CHAIR_PRICE + (3/4)*JOYSTICK_PRICE

    # Calculate the difference between Frank's and Eman's payments
    difference = frank_payment - eman_payment

    # Display the difference
    result = difference
    return result

print(solution())