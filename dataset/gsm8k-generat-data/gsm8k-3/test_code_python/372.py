def solution():
    """Nurse Missy is attending to the needs of 12 patients in her hospital ward.  Most of her patients require standard care, but one-third of her patients have special dietary requirements, which increases the serving time by 20%.  At dinner time, she brings each patient their meal. It takes 5 minutes to serve each standard care patient.  How long does it take, in minutes, for Missy to serve dinner to all of her patients?"""
    # Define the number of patients with special dietary requirements
    special_requirement_patients = 12 // 3

    # Calculate the extra serving time for those patients
    extra_time = 5 * 0.2

    # Add the extra time to the serving time for those patients
    special_serve_time = 5 + extra_time

    # Calculate the total serving time for all patients
    total_serve_time = (12 - special_requirement_patients) * 5 + special_requirement_patients * special_serve_time

    # Display the total serving time
    result = total_serve_time
    return result

print(solution())