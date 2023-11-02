def solution():
    initial_enrollment = 8
    new_interest = 8
    new_dropouts = new_interest // 4
    remaining_new = new_interest - new_dropouts
    frustrated_dropouts = 2
    total_enrollment = initial_enrollment + remaining_new - new_dropouts - frustrated_dropouts
    increased_enrollment = total_enrollment * 5
    scheduling_conflicts = 2
    total_enrollment = increased_enrollment - scheduling_conflicts
    half_dropouts = total_enrollment // 2
    remaining_enrollment = total_enrollment - half_dropouts
    graduates = remaining_enrollment // 2
    still_enrolled = remaining_enrollment - graduates
    result = still_enrolled
    return result

print(solution())