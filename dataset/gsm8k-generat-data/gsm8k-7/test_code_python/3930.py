def solution():
    jonsey_awake_time = 2/3
    riley_awake_time = 3/4

    jonsey_outside_time = jonsey_awake_time * 1/2
    jonsey_inside_time = jonsey_awake_time - jonsey_outside_time

    riley_outside_time = riley_awake_time * 1/3
    riley_inside_time = riley_awake_time - riley_outside_time

    # Calculate the average time they spend inside
    avg_inside_time = (jonsey_inside_time + riley_inside_time) / 2
    result = avg_inside_time
    return result

print(solution())