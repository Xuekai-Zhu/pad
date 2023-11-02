def solution():
    # Define the relevant dates
    war_in_vietnam_1945_start = 1945
    war_in_vietnam_1945_end = 1946
    vietnam_war_with_america_start = 1955
    # Check if veterans of the War in Vietnam (1945-46) were given free education by the Soviet Union
    if vietnam_war_with_america_start - war_in_vietnam_1945_end >= 20:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())