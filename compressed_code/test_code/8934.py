def solution():
    
    total_students = 250
    basketball_percentage = 0.4
    chess_percentage = 0.1
    soccer_percentage = 0.28
    badminton_percentage = 1 - basketball_percentage - chess_percentage - soccer_percentage
    basketball_students = int(basketball_percentage * total_students)
    chess_students = int(chess_percentage * total_students)
    result = basketball_students + chess_students
    return result

print(solution())