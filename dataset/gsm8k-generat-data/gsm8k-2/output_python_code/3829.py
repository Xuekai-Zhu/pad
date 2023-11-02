def solution():
    """A psychologist believes one in every four people has a disorder he calls ZYX syndrome. The clinic where he works has recently doubled its previous number of 26 patients. How many patients is the psychologist likely to diagnose with ZYX syndrome?"""
    patients = 2 * 26
    zyx_patients = patients / 4
    result = zyx_patients
    return result

print(solution())