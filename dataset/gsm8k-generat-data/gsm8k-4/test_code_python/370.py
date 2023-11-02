def solution():
    """Nurse Missy is attending to the needs of 12 patients in her hospital ward. Most of her patients require standard care, but one-third of her patients have special dietary requirements, which increases the serving time by 20%. At dinner time, she brings each patient their meal. It takes 5 minutes to serve each standard care patient. How long does it take, in minutes, for Missy to serve dinner to all of her patients?"""
    # Define the number of patients and the time it takes to serve a standard care patient
    NUM_PATIENTS = 12
    STDCARE_TIME = 5

    # Calculate the number of patients with special dietary requirements
    specialcare_patients = NUM_PATIENTS // 3

    # Calculate the total time to serve all patients with special care requirements
    specialcare_time = specialcare_patients * STDCARE_TIME * 1.2

    # Calculate the total time to serve all standard care patients
    stdcare_patients = NUM_PATIENTS - specialcare_patients
    stdcare_time = stdcare_patients * STDCARE_TIME

    # Calculate the total time to serve all patients
    total_time = specialcare_time + stdcare_time

    # return the result
    result = total_time
    return result

print(solution())