def solution():
    """Nurse Missy is attending to the needs of 12 patients in her hospital ward. Most of her patients require standard care, but one-third of her patients have special dietary requirements, which increases the serving time by 20%. At dinner time, she brings each patient their meal. It takes 5 minutes to serve each standard care patient. How long does it take, in minutes, for Missy to serve dinner to all of her patients?"""
    num_patients = 12
    num_special = num_patients // 3
    standard_time = 5
    special_time = standard_time * 1.2
    total_time = (num_patients - num_special) * standard_time + num_special * special_time
    result = total_time
    return result

print(solution())