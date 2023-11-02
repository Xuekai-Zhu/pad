def solution():
     Sammy_score = 20
     Gab_score = Sammy_score * 2
     Cher_score = Gab_score * 2
     total_score = Sammy_score + Gab_score + Cher_score
     opponent_score = 85
     points_difference = total_score - opponent_score
     result = points_difference
     return result

print(solution())