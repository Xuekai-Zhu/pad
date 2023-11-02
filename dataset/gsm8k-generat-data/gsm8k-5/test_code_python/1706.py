def solution():
    total_students = 400  # There are 400 students in the senior class
    sports_players = 0.52 * total_students  # 52% of the students play sports
    soccer_players = 0.125 * sports_players  # 12.5% of sports players play soccer
    result = soccer_players
    return result

print(solution())