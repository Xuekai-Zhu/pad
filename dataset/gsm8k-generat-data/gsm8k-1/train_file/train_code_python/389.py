def solution():
    """Oscar wants to train for a marathon. He plans to add 2/3 of a mile each week until he reaches a 20-mile run. How many weeks before the marathon should he start training if he has already run 2 miles?"""
    starting_distance = 2
    goal_distance = 20
    
    weekly_increase = 2/3
    
    # Calculate number of weeks by dividing the remaining distance by the weekly increase
    weeks = (goal_distance - starting_distance) / weekly_increase
    result = weeks
    
    return result

print(solution())