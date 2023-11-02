def solution():
    """A psychologist believes one in every four people has a disorder he calls ZYX syndrome. The clinic where he works has recently doubled its previous number of 26 patients. How many patients is the psychologist likely to diagnose with ZYX syndrome?"""
    # Define the proportion of people with ZYX syndrome
    zyx_proportion = 0.25

    # Define the number of patients at the clinic
    previous_patients = 26

    # Double the number of patients
    current_patients = previous_patients * 2

    # Calculate the expected number of patients with ZYX syndrome
    zyx_patients = current_patients * zyx_proportion

    # Round to the nearest whole number
    result = round(zyx_patients)
    return result

print(solution())