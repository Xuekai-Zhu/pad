def solution():
    jonsey_awake_time = 2/3  # Jonsey is awake for 2/3 of the day
    jonsey_outside_time = 1/2 * jonsey_awake_time  # Jonsey spends 1/2 of her awake time playing outside
    jonsey_inside_time = jonsey_awake_time - jonsey_outside_time  # Jonsey spends the rest of her awake time inside

    riley_awake_time = 3/4  # Riley is awake for 3/4 of the day
    riley_outside_time = 1/3 * riley_awake_time  # Riley spends 1/3 of his awake time playing outside
    riley_inside_time = riley_awake_time - riley_outside_time  # Riley spends the rest of his awake time inside

    # Calculate the average time they spend inside
    avg_inside_time = (jonsey_inside_time + riley_inside_time) / 2
    result = avg_inside_time
    return result

print(solution())