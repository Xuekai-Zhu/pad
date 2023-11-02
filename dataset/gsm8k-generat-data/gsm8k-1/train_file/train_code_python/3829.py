def solution():
    """A psychologist believes one in every four people has a disorder he calls ZYX syndrome. The clinic where he works has recently doubled its previous number of 26 patients. How many patients is the psychologist likely to diagnose with ZYX syndrome?"""
    ZYX_percentage = 0.25
    total_patients = 26 * 2
    patients_with_ZYX = ZYX_percentage * total_patients
    result = patients_with_ZYX
    return result

print(solution())