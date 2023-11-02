def solution():
    ann_age = 6
    tom_age = ann_age * 2
    years_later = 10
    ann_future_age = ann_age + years_later
    tom_future_age = tom_age + years_later
    total_future_age = ann_future_age + tom_future_age
    result = total_future_age
    return result

print(solution())