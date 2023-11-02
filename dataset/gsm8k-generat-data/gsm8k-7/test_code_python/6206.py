def solution():
    table_cost = 140
    chair_cost = 100
    joystick_cost = 20

    # Frank pays for the table
    frank_total = table_cost

    # Eman pays for the chair and part of the joystick
    eman_total = chair_cost + (3/4 * joystick_cost)

    # Calculate the difference
    difference = frank_total - eman_total
    result = difference
    return result

print(solution())