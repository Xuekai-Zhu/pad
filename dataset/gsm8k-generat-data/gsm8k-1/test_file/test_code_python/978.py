def solution():
    """In Mr. Roper's class of 30 students, 20% of the class are football players. Out of the remaining class, 25% of the students are cheerleaders or part of band. These 3 groups of students will need to leave early today to travel to an away game. How many students are leaving early?"""
    class_size = 30
    football_players = int(class_size*0.2)
    remaining_students = class_size - football_players
    cheerleaders_or_band = int(remaining_students*0.25)
    students_leaving = football_players + cheerleaders_or_band
    result = students_leaving
    return result

print(solution())