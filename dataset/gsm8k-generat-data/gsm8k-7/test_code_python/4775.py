def solution():
    current_age_matt = 5
    age_difference = 7
    future_age_kaylee = current_age_matt * 3 + age_difference

    # Calculate the current age of Kaylee
    current_age_kaylee = future_age_kaylee - age_difference
    result = current_age_kaylee
    return result

print(solution())