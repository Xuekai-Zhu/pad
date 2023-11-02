def solution():
    total_students = 180
    deaf_students = 3 * blind_students
    total_deaf_and_blind = deaf_students + blind_students
    blind_students = total_students / (3 + 1) # 3 times as many deaf students as blind students
    result = blind_students
    return result

print(solution())