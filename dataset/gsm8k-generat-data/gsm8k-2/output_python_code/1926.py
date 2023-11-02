def solution():
    """Mike and Leo have to print as many pamphlets as possible for a social gathering. Mike manages to print as fast as 600 pamphlets per hour for 9 consecutive hours. After a break, he resumes the task for another 2 hours achieving a third of the speed he was doing before. Leo, on the other hand, only works a third as many hours as Mike did before his break, but was twice as fast as Mike before he took his break. How many pamphlets do both manage to print at the end?"""
    mike_hours_1 = 9
    mike_speed_1 = 600
    mike_pamphlets_1 = mike_hours_1 * mike_speed_1
    
    mike_hours_2 = 2
    mike_speed_2 = mike_speed_1 / 3
    mike_pamphlets_2 = mike_hours_2 * mike_speed_2
    
    leo_hours = mike_hours_1 / 3
    leo_speed = 2 * mike_speed_1
    leo_pamphlets = leo_hours * leo_speed
    
    total_pamphlets = mike_pamphlets_1 + mike_pamphlets_2 + leo_pamphlets
    result = total_pamphlets
    return result

print(solution())