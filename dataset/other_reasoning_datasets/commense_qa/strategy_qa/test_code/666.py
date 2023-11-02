def solution():
    abba_gender_config = ["male", "male", "female", "female"]
    mamas_papas_gender_config = ["male", "male", "female", "female"]
    if abba_gender_config == mamas_papas_gender_config:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())