def solution():
     gym_hours_per_week = 3
     boxing_hours_per_week = 4
     strength_training_hours_per_session = 1
     boxing_hours_per_session = 1.5
     total_hours_trained_per_week = (gym_hours_per_week * strength_training_hours_per_session) + (boxing_hours_per_week * boxing_hours_per_session)
     result = total_hours_trained_per_week
     return result

print(solution())