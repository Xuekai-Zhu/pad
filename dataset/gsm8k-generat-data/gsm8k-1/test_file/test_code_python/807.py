def solution():
    """Felix notices that kids in the neighborhood are always getting things stuck in trees. Since he is an expert tree climber, he decided to start charging kids to get their stuff out. He charges based on how high he has to climb. Every branch he has to climb up costs $.25. During the week he made $105. On average, how many branches did he climb per day?"""
    money_made = 105
    cost_per_branch = 0.25
    branches_climbed = money_made / cost_per_branch
    days_in_week = 7
    branches_per_day = branches_climbed / days_in_week
    
    result = branches_per_day
    return result

print(solution())