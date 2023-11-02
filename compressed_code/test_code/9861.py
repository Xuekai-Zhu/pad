def solution():
    
    states_collected = 40
    total_states = 50
    percent_collected = states_collected / total_states * 100
    earning_per_percent = 2
    total_earning = percent_collected * earning_per_percent
    result = total_earning
    return result

print(solution())