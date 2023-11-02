def solution():
    """John works at 2 different hospitals. At the first hospital, he sees 20 different patients each day. At the second hospital, he sees 20% more individual patients a day. He works 5 days a week. How many patients does he treat a year if he works 50 weeks a year?"""
    patients_per_day_first_hospital = 20
    patients_per_day_second_hospital = round(patients_per_day_first_hospital * 1.2)
    days_per_week = 5
    weeks_per_year = 50
    total_patients_treated = (patients_per_day_first_hospital + patients_per_day_second_hospital) * days_per_week * weeks_per_year
    result = total_patients_treated
    return result

print(solution())