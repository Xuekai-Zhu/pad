def solution():
    """Two siblings, Eman and Frank, agreed to buy a new computer table, computer chair, and a joystick. The computer table costs $140, the computer chair costs $100, and the joystick costs $20. Eman agreed to pay for the computer chair while Frank agreed to pay for the computer table. Then Frank agreed to pay 1/4 of the price of the joystick and the rest will be paid by Eman. How much more money will Frank spend than Eman?"""
    computer_table = 140
    computer_chair = 100
    joystick = 20
    frank_joystick_contribution = joystick / 4
    frank_total_cost = computer_table + frank_joystick_contribution
    eman_total_cost = computer_chair + (joystick - frank_joystick_contribution)
    difference = frank_total_cost - eman_total_cost
    result = difference
    
    return result

print(solution())