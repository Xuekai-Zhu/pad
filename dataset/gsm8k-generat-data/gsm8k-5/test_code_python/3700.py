def solution():
    caps_per_minute_A = 12  # Machine A can cap 12 bottles in 1 minute
    caps_per_minute_B = caps_per_minute_A - 2  # Machine B caps 2 fewer bottles than Machine A
    caps_per_minute_C = caps_per_minute_B + 5  # Machine C caps 5 more bottles than Machine B
    minutes = 10  # We want to find out how many bottles can be capped in 10 minutes

    # Calculate the total number of bottles capped by all three machines in 1 minute
    total_caps_per_minute = caps_per_minute_A + caps_per_minute_B + caps_per_minute_C

    # Calculate the total number of bottles capped in 10 minutes
    total_caps = total_caps_per_minute * minutes
    result = total_caps
    return result

print(solution())