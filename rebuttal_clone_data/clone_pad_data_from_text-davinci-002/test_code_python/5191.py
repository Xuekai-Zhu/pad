def solution():
     total_states = 51
     states_collected = 40
     percent_collected = (states_collected / total_states) * 100
     money_earned = percent_collected * 2
     result = money_earned
     return result

print(solution())