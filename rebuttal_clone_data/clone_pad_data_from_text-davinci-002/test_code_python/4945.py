def solution():
     total_cows = 300
     male_cows = total_cows / 2
     female_cows = total_cows / 2
     spotted_females = female_cows / 2
     males_with_horns = male_cows / 2
     difference = spotted_females - males_with_horns
     result = difference
     return result

print(solution())