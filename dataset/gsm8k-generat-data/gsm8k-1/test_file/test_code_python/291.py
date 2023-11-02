def solution():
    """Darren decides to do body exercises for a whole week. He does 100 pushups, 50 squats, and 20 dumbbell presses on the first day. On the second day, he does 20 more pushups than on the first day, ten fewer squats, and doubles the number of dumbbell presses. What's the total count of the activities he's done in the two days?"""
    pushups_day_1 = 100
    squats_day_1 = 50
    dumbbell_presses_day_1 = 20
    
    pushups_day_2 = pushups_day_1 + 20
    squats_day_2 = squats_day_1 - 10
    dumbbell_presses_day_2 = dumbbell_presses_day_1 * 2
    
    total_pushups = pushups_day_1 + pushups_day_2
    total_squats = squats_day_1 + squats_day_2
    total_dumbbell_presses = dumbbell_presses_day_1 + dumbbell_presses_day_2
    
    total_count = total_pushups + total_squats + total_dumbbell_presses
    
    return total_count

print(solution())