def solution():
    
    day1_pushups = 100
    day1_squats = 50
    day1_dumbbell_presses = 20
    day2_pushups = day1_pushups + 20
    day2_squats = day1_squats - 10
    day2_dumbbell_presses = day1_dumbbell_presses * 2
    total_activities = day1_pushups + day1_squats + day2_dumbbell_presses + day2_pushups + day2_squats + day2_dumbbell_presses
    result = total_activities
    return result

print(solution())