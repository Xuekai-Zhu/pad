def solution():
    """The ski lift carries skiers all the way from the bottom of the mountain to the very top of the mountain, and then drops them off so they can ski back down the mountain. If it takes a skier 15 minutes to ride the lift from the bottom to the top of the mountain, and then it takes 5 minutes to ski back down the mountain, what is the most number of times a person can ski down the mountain in 2 hours?"""
    total_time = 120 # 2 hours in minutes
    lift_time = 15
    ski_time = 5
    total_cycle_time = lift_time + ski_time
    cycles_per_hour = 60 // total_cycle_time
    total_cycles = cycles_per_hour * 2
    result = total_cycles
    return result

print(solution())