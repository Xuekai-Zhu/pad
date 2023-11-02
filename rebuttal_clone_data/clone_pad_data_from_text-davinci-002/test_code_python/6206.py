def solution():
     computer_table = 140
     computer_chair = 100
     joystick = 20
     total_price = computer_table + computer_chair + joystick
     Eman_share = total_price - computer_chair
     Frank_share = total_price - joystick - Eman_share
     result = Frank_share - Eman_share
     return result

print(solution())