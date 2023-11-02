def solution():
    
    orlando_gain = 5
    jose_gain = 2 + 2*orlando_gain
    fernando_gain = (0.5*jose_gain) - 3
    total_gain = orlando_gain + jose_gain + fernando_gain
    result = total_gain
    return result

print(solution())