def solution():
    """Paul is collecting license plates from different states. He has plates from 40 different states. For each percentage point of total US states that he has, his parents will give him $2. How much does he earn from them?"""
    states_collected = 40
    total_states = 50
    percent_collected = states_collected / total_states * 100
    earning_per_percent = 2
    total_earning = percent_collected * earning_per_percent
    result = total_earning
    return result

print(solution())