def solution():
    """Nurse Missy is attending to the needs of 12 patients in her hospital ward. Most of her patients require standard care, but one-third of her patients have special dietary requirements, which increases the serving time by 20%. At dinner time, she brings each patient their meal. It takes 5 minutes to serve each standard care patient. How long does it take, in minutes, for Missy to serve dinner to all of her patients?"""
    total_patients = 12
    standard_care_patients = 8
    special_diet_patients = total_patients - standard_care_patients
    special_diet_time = 1.2 * 5 # 20% longer than standard care
    total_time = (standard_care_patients * 5) + (special_diet_patients * special_diet_time)
    result = total_time
    return result

print(solution())