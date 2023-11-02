def solution():
    # Calculate the total amount of time in a day
    total_time = 24  # there are 24 hours in a day

    # Calculate the total amount of time Steve spends on sleeping, school, and making assignments
    study_time = (1/3) + (1/6) + (1/12)
    
    # Calculate the amount of time Steve spends with his family
    family_time = total_time - (study_time * total_time)
    result = family_time
    return result

print(solution())