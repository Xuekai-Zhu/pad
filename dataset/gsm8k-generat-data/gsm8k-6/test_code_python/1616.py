def solution():
    # Calculate the total study time from Monday to Friday
    total_study_MonFri = 4 + 2*4 + 3*3  # studies for 4 hours on Monday, twice as long on Tuesday, and 3 hours each on Wednesday, Thursday, and Friday

    # Determine the remaining study time required to reach the goal of 25 hours
    remaining_study_time = 25 - total_study_MonFri  

    # Divide the remaining study time equally between Saturday and Sunday
    study_time_SatSun = remaining_study_time / 2  

    result = study_time_SatSun
    return result

print(solution())