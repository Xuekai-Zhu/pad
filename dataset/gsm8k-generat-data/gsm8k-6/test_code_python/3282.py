def solution():
    # Calculate the current age of Mark
    current_year = 2021
    mark_birth_year = 1976
    age_mark = current_year - mark_birth_year

    # Calculate the age of Graham
    age_graham = age_mark - 3  

    # Calculate the age of Janice
    age_janice = age_graham / 2

    result = age_janice
    return result

print(solution())