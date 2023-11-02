def solution():
    """Paul is collecting license plates from different states. He has plates from 40 different states. For each percentage point of total US states that he has, his parents will give him $2. How much does he earn from them?"""
    total_states = 50
    collected_states = 40
    percentage_collected = (collected_states / total_states) * 100
    earnings = percentage_collected * 2
    result = earnings
    return result

print(solution())