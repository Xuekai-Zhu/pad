def solution():
    future_half_age = 80 / 2 / 2  # Christina's future half age in 5 years
    christina_now = future_half_age - 5  # Christina's current age
    oscar_future = 3/5 * christina_now + 15  # Oscar's age in 15 years
    oscar_now = oscar_future - 15  # Oscar's current age
    result = oscar_now
    return result

print(solution())