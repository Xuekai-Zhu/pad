def solution():
    Saturday_attendance = 80
    Monday_attendance = Saturday_attendance - 20
    Wednesday_attendance = Monday_attendance + 50
    Friday_attendance = Saturday_attendance + Monday_attendance
    expected_ Attedance = 350
    actual_attendance = Friday_attendance
    result = actual_attendance - expected_attendance
    
    return result

print(solution())