def solution():
    """Courtney attended a concert and reported that the audience was 48 in number. However, Kelly went to the same concert and said that Courtney had made the mistake of overstating the number of people in attendance by 20%. If Kelly was right, how many people really attended the concert?"""
    reported_attendance = 48
    overstatement_percent = 20
    actual_attendance = reported_attendance / (1 + (overstatement_percent / 100))
    result = actual_attendance
    return result

print(solution())