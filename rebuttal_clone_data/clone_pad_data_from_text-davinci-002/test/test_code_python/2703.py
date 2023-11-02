def solution():
    jellybeans = 100
    normal_attendance = 24
    absent_students = 2
    attending_students = normal_attendance - absent_students
    jellybeans_eaten = attending_students * 3
    jellybeans_left = jellybeans - jellybeans_eaten
    result = jellybeans_left
    return result

print(solution())