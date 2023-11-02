def solution():
    current_age_matt = 5  # Matt is currently 5 years old
    years_to_add = 7  # In 7 years
    required_multiple = 3  # Kaylee will be 3 times as old as Matt

    # Calculate Kaylee's current age using the given age ratio
    current_age_kaylee = required_multiple * (current_age_matt + years_to_add) - years_to_add
    result = current_age_kaylee
    return result

print(solution())