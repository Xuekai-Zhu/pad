def solution():
    """Mike and Leo have to print as many pamphlets as possible for a social gathering. Mike prints 600 pamphlets per hour for 9 hours, takes a break, then prints for 2 more hours at a third of the previous speed. Leo works for a third as long as Mike but is twice as fast as Mike before the break. How many pamphlets do both manage to print at the end?"""
    mike_speed = 600
    mike_hours_1 = 9
    mike_hours_2 = 2
    leo_speed = 2 * mike_speed
    leo_hours = mike_hours_1 / 3
    
    mike_pamphlets_1 = mike_speed * mike_hours_1
    mike_pamphlets_2 = (mike_speed / 3) * mike_hours_2
    leo_pamphlets = leo_speed * leo_hours
    
    total_pamphlets = mike_pamphlets_1 + mike_pamphlets_2 + leo_pamphlets
    result = total_pamphlets
    return result

print(solution())