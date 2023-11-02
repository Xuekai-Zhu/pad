def solution():
    """Two siblings, Eman and Frank, agreed to buy a new computer table, computer chair, and a joystick. The computer table costs $140, the computer chair costs $100, and the joystick costs $20. Eman agreed to pay for the computer chair while Frank agreed to pay for the computer table. Then Frank agreed to pay 1/4 of the price of the joystick and the rest will be paid by Eman. How much more money will Frank spend than Eman?"""
    table_cost = 140
    chair_cost = 100
    joystick_cost = 20
    frank_share = table_cost
    emman_share = chair_cost + (joystick_cost - (joystick_cost/4))
    diff = frank_share - emman_share
    result = diff
    return result

print(solution())