def solution():
    """Mike and Leo have to print as many pamphlets as possible for a social gathering. Mike manages to print as fast as 600 pamphlets per hour for 9 consecutive hours. After a break, he resumes the task for another 2 hours achieving a third of the speed he was doing before. Leo, on the other hand, only works a third as many hours as Mike did before his break, but was twice as fast as Mike before he took his break. How many pamphlets do both manage to print at the end?"""
    
    # Mike's print rate in pamphlets per hour
    mike_rate = 600
    
    # Number of hours worked by Mike before the break
    mike_hours_before_break = 9
    
    # Total pamphlets printed by Mike before the break
    mike_total_before_break = mike_rate * mike_hours_before_break
    
    # Number of hours worked by Mike after the break
    mike_hours_after_break = 2
    
    # Mike's print rate after the break
    mike_rate_after_break = mike_rate / 3
    
    # Total pamphlets printed by Mike after the break
    mike_total_after_break = mike_rate_after_break * mike_hours_after_break
    
    # Total pamphlets printed by Mike
    mike_total_pamphlets = mike_total_before_break + mike_total_after_break
    
    # Number of hours worked by Leo
    leo_hours = mike_hours_before_break / 3
    
    # Leo's print rate in pamphlets per hour
    leo_rate = mike_rate * 2
    
    # Total pamphlets printed by Leo
    leo_total_pamphlets = leo_rate * leo_hours
    
    # Total pamphlets printed by both
    total_pamphlets = mike_total_pamphlets + leo_total_pamphlets
    
    return total_pamphlets

print(solution())