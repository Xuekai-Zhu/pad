def solution():
    kwame_hours = 2.5
    connor_hours = 1.5
    lexia_minutes = 97

    # Convert all study times to minutes
    kwame_minutes = kwame_hours * 60
    connor_minutes = connor_hours * 60

    # Calculate the total study time for Kwame and Connor
    total_kc_minutes = kwame_minutes + connor_minutes

    # Calculate the difference between the total study time for Kwame and Connor and Lexia's study time
    difference = total_kc_minutes - lexia_minutes
    result = difference
    return result

print(solution())