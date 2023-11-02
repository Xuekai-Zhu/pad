def solution():
    """For 6 weeks in the summer, Erica treats herself to 1 ice cream cone from the ice cream truck. 
    Monday, Wednesday and Friday she gets a $2.00 orange creamsicle. 
    Tuesday and Thursday she gets a $1.50 ice cream sandwich. 
    Saturday and Sunday she gets a $3.00 Nutty-Buddy. How much money does she spend on ice cream in 6 weeks?"""
    creamsicle_cost = 2
    sandwich_cost = 1.5
    nutty_buddy_cost = 3
    
    days_per_week = 7
    cones_per_week = 7
    
    creamsicles_per_week = 3
    sandwiches_per_week = 2
    nutty_buddies_per_week = 2
    
    total_cost = (creamsicles_per_week * creamsicle_cost + sandwiches_per_week * sandwich_cost 
                  + nutty_buddies_per_week * nutty_buddy_cost) * cones_per_week
    
    total_cost_6_weeks = total_cost * 6
    
    result = total_cost_6_weeks
    
    return result

print(solution())