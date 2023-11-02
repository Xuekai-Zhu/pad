def solution():
    """Felix can lift off the ground 1.5 times more than he weighs. Felix's brother weighs twice as much as Felix
    and can lift three times his weight off the ground. If his brother can lift 600 pounds, how much can Felix lift 
    off the ground?"""
    
    # Let Felix's weight be x
    x = 0
    
    # Felix's brother weighs twice as much as Felix
    brother_weight = x*2
    
    # Felix's brother can lift three times his weight off the ground
    brother_lift = brother_weight*3
    
    # If his brother can lift 600 pounds, brother_lift = 600
    brother_lift = 600
    
    # so brother_weight = brother_lift / 3
    brother_weight = brother_lift / 3
    
    # Since Felix can lift off the ground 1.5 times more than he weighs
    felix_lift = (1.5*x) + x
    
    # Results
    result = felix_lift
    return result

print(solution())