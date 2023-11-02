def solution():
     daily_steps = 1000
     weekly_increase = 1000
     total_steps = 4 * (daily_steps + (4 - 1) * weekly_increase)
     goal_steps = 100000
     steps_away = goal_steps - total_steps
     
     return steps_away

print(solution())