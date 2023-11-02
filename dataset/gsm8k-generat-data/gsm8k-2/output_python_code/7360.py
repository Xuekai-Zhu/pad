def solution():
    """John works at 2 different hospitals. At the first hospital, he sees 20 different patients each day. At the second hospital, he sees 20% more individual patients a day. He works 5 days a week. How many patients does he treat a year if he works 50 weeks a year?"""
    first_hospital_patients_per_week = 20 * 5
    second_hospital_patients_per_week = round(1.2 * 20) * 5
    total_patients_per_week = first_hospital_patients_per_week + second_hospital_patients_per_week
    total_patients_per_year = total_patients_per_week * 50
    result = total_patients_per_year
    return result

print(solution())