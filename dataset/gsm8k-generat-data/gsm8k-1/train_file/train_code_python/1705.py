def solution():
    """There are 400 students in the senior class at East High School. 52% of the students play sports. Of the students that play sports, 12.5% play soccer. How many students play soccer?"""
    total_students = 400
    sports_percent = 52
    soccer_percent = 12.5
    sports_students = total_students * (sports_percent / 100)
    soccer_players = sports_students * (soccer_percent / 100)
    result = soccer_players
    return result

print(solution())