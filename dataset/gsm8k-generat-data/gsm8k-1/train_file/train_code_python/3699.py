def solution():
    """There are three machines in a factory. Machine A can put caps on 12 bottles in 1 minute. Machine B can put caps to 2 fewer bottles than Machine A. Machine C can put caps to 5 more bottles than Machine B. How many bottles can those three machines put caps on in 10 minutes?"""
    caps_per_minute_A = 12
    caps_per_minute_B = caps_per_minute_A - 2
    caps_per_minute_C = caps_per_minute_B + 5
    total_caps_per_minute = caps_per_minute_A + caps_per_minute_B + caps_per_minute_C
    total_caps_in_10_min = total_caps_per_minute * 10
    result = total_caps_in_10_min
    return result

print(solution())