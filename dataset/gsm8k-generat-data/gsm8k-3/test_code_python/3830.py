def solution():
    """A psychologist believes one in every four people has a disorder he calls ZYX syndrome. The clinic where he works has recently doubled its previous number of 26 patients. How many patients is the psychologist likely to diagnose with ZYX syndrome?"""
    # Define the probability of a person having ZYX syndrome
    ZYX_PROBABILITY = 0.25

    # Define the number of patients at the clinic before it doubled
    pre_doubled_patients = 26

    # Calculate the total number of patients after the clinic doubled
    total_patients = pre_doubled_patients * 2

    # Calculate the expected number of patients with ZYX syndrome
    expected_patients = total_patients * ZYX_PROBABILITY

    # Display the expected number of patients
    result = expected_patients
    return result

print(solution())