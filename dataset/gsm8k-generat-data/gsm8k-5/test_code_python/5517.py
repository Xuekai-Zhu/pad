def solution():
    kwame_study_time = 2.5 * 60  # Kwame studied for 2.5 hours, converted to minutes
    connor_study_time = 1.5 * 60  # Connor studied for 1.5 hours, converted to minutes
    lexia_study_time = 97  # Lexia studied for 97 minutes

    # Calculate total study time for Kwame and Connor
    total_kc_study_time = kwame_study_time + connor_study_time

    # Calculate the difference between total study time for Kwame and Connor and Lexia's study time
    difference = total_kc_study_time - lexia_study_time

    result = difference
    return result

print(solution())