def solution():
    """Mrs. Carlton gives out penalty points whenever her students misbehave. They get 5 points for interrupting, 10 points for insulting their classmates, and 25 points for throwing things. 
    If they get 100 points, they have to go to the office. Jerry already interrupted twice and insulted his classmates 4 times. How many times can he throw things before he gets sent to the office?"""
    
    points_for_interruption = 5
    points_for_insulting = 10
    points_for_throwing = 25
    
    total_points = points_for_interruption * 2 + points_for_insulting * 4
    
    remaining_points = 100 - total_points
    
    times_can_throw = remaining_points // points_for_throwing
    
    result = times_can_throw
    
    return result

print(solution())