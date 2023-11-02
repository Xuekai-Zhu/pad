def solution():
    """Mike and Leo have to print as many pamphlets as possible for a social gathering. Mike manages to print as fast as 600 pamphlets per hour for 9 consecutive hours. After a break, he resumes the task for another 2 hours achieving a third of the speed he was doing before. Leo, on the other hand, only works a third as many hours as Mike did before his break, but was twice as fast as Mike before he took his break. How many pamphlets do both manage to print at the end?"""
    # Calculate Mike's pamphlets printed in the first 9 hours
    mike_first_hours = 9
    mike_first_speed = 600
    mike_first_pamphlets = mike_first_hours * mike_first_speed

    # Calculate Mike's pamphlets printed in the last 2 hours
    mike_last_hours = 2
    mike_last_speed = mike_first_speed / 3
    mike_last_pamphlets = mike_last_hours * mike_last_speed

    # Calculate Leo's pamphlets printed
    leo_hours = mike_first_hours / 3
    leo_speed = mike_first_speed * 2
    leo_pamphlets = leo_hours * leo_speed

    # Calculate the total pamphlets printed
    total_pamphlets = mike_first_pamphlets + mike_last_pamphlets + leo_pamphlets

    # Display the total pamphlets printed
    result = total_pamphlets
    return result

print(solution())