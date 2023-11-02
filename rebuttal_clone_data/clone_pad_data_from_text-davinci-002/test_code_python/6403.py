def solution():
     shots_per_day = 200
     days_per_week = 4
     percentage_recovered = 20
     percentage_paid_by_team = 70
     cost_per_arrow = 5.5
     arrows_shot_per_week = shots_per_day * days_per_week
     arrows_recovered_per_week = arrows_shot_per_week * (percentage_recovered / 100)
     arrows_paid_for_by_team_per_week = arrows_shot_per_week * (percentage_paid_by_team / 100)
     cost_per_week = (arrows_shot_per_week - arrows_recovered_per_week - arrows_paid_for_by_team_per_week) * cost_per_arrow
     result = cost_per_week
     return result

print(solution())