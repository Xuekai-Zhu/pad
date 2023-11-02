def solution():
    """A dental office gives away 2 toothbrushes to every patient who visits. His 8 hour days are packed and each visit takes .5 hours. How many toothbrushes does he give in a 5-day work week?"""
    toothbrushes_per_patient = 2
    visits_per_day = 16
    visit_time = 0.5
    days_per_week = 5
    total_visits = visits_per_day * 8 * days_per_week
    total_patients = total_visits / visit_time
    total_toothbrushes = total_patients * toothbrushes_per_patient
    result = total_toothbrushes
    return result

print(solution())