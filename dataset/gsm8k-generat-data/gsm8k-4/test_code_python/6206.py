def solution():
    """Two siblings, Eman and Frank, agreed to buy a new computer table, computer chair, and a joystick. The computer table costs $140, the computer chair costs $100, and the joystick costs $20. Eman agreed to pay for the computer chair while Frank agreed to pay for the computer table. Then Frank agreed to pay 1/4 of the price of the joystick and the rest will be paid by Eman. How much more money will Frank spend than Eman?"""
    # Define the prices of the computer table, computer chair, and joystick
    table_price = 140
    chair_price = 100
    joystick_price = 20

    # Calculate the amount Frank will pay for the joystick
    joystick_split = joystick_price / 4
    frank_joystick = joystick_split + table_price

    # Calculate the amount Eman will pay for the joystick
    eman_joystick = joystick_price - joystick_split + chair_price

    # Calculate the total amount spent by Frank and Eman
    total_frank = frank_joystick + chair_price
    total_eman = eman_joystick + table_price

    # Calculate how much more Frank spent than Eman
    difference = total_frank - total_eman

    # Return the result
    result = difference
    return result

print(solution())