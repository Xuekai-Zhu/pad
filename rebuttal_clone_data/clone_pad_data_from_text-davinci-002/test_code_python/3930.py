def solution():
    jonsey_awake_fraction = 2/3
    jonsey_inside_fraction = 1 - (1/2)
    riley_awake_fraction = 3/4
    riley_inside_fraction = 1 - (1/3)
    total_inside_fraction = (jonsey_awake_fraction * jonsey_inside_fraction) + (riley_awake_fraction * riley_inside_fraction)
    result = total_inside_fraction
    return result

print(solution())