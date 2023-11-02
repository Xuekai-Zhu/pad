def solution():
    # Find Xavier's current age
    xavier_in_six_years = 30
    xavier_current_age = xavier_in_six_years - 6
    # Find Yasmin's current age
    yasmin_current_age = xavier_current_age / 2
    # Find the total of their ages
    total_age = xavier_current_age + yasmin_current_age
    result = total_age
    return result

print(solution())