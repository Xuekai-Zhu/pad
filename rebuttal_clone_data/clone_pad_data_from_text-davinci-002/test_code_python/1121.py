def solution():
    current_age_difference = 60
    pens_owned = 60
    Clara_pens = pens_owned * (2/5)
    future_age_difference = current_age_difference + 5
    future_pens = future_age_difference * (2/5)
    Clara_future_age = future_pens + 20
    result = Clara_future_age
    return result

print(solution())