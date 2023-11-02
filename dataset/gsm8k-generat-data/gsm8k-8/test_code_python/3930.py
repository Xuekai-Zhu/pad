def solution():
    # Calculate the amount of time Jonsey spends awake
    jonsey_awake_time = (2/3) * 24 # 24 is the number of hours in a day

    # Calculate the amount of time Jonsey spends playing outside
    jonsey_outside_time = (1/2) * jonsey_awake_time

    # Calculate the amount of time Jonsey spends inside
    jonsey_inside_time = jonsey_awake_time - jonsey_outside_time

    # Calculate the amount of time Riley spends awake
    riley_awake_time = (3/4) * 24

    # Calculate the amount of time Riley spends playing outside
    riley_outside_time = (1/3) * riley_awake_time

    # Calculate the amount of time Riley spends inside
    riley_inside_time = riley_awake_time - riley_outside_time

    # Calculate the average time they spend inside
    average_inside_time = (jonsey_inside_time + riley_inside_time) / 2
    result = average_inside_time
    return result

print(solution())