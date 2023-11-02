def solution():
    
    normal_teacher_chance = 0.5
    personal_teacher_chance = 0.2
    normal_teacher_total_chance = normal_teacher_chance * 1.4
    tomorrow_total_chance = tomorrow_total_chance * 1.2
    total_chance = normal_teacher_total_chance + tomorrow_total_chance
    percentage_chance = (total_chance / total_chance) * 100
    result = percentage_chance
    return result

print(solution())