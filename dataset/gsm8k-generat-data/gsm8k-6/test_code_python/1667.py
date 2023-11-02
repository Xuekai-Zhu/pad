def solution():
    # Calculate the average number of streets patrolled per hour by officer A and B
    streets_per_hour_A = 36/4  # Officer A patrols 36 streets in 4 hours
    streets_per_hour_B = 55/5  # Officer B patrols 55 streets in 5 hours
    streets_per_hour_both = streets_per_hour_A + streets_per_hour_B  # Total streets patrolled by both officers in one hour
    result = streets_per_hour_both
    return result

print(solution())