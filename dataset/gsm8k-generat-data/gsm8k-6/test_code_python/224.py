def solution():
    age_first_scroll = 4080  # age of the first scroll

    # Calculate the age of each scroll using a loop
    age_last_scroll = age_first_scroll
    for i in range(1, 5):
        age_current_scroll = age_last_scroll + age_last_scroll / 2
        age_last_scroll = age_current_scroll

    result = int(age_last_scroll)  # round down age to nearest integer
    return result

print(solution())