def solution():
    """A dance studio offers lessons to students. It costs $25 per session to rent the studio plus $1.50 per student per session. At present, the dance studio has 10 students and is rented 3 days a week. How much are the expected earnings of the dance studio in a month?"""
    rent_per_session = 25
    students_per_session = 10
    price_per_student = 1.5
    sessions_per_week = 3
    weeks_per_month = 4
    total_sessions = sessions_per_week * weeks_per_month
    total_students = students_per_session * total_sessions
    earnings_per_session = rent_per_session + (price_per_student * students_per_session)
    total_earnings = earnings_per_session * total_sessions
    result = total_earnings
    
    return result

print(solution())