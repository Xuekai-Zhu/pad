def solution():
    # Calculate the number of judges in each age group
    young_judges = 0.1 * 40  # 10% of judges are under 30 years old
    middle_judges = 0.6 * 40  # 60% of judges are between 30 and 50 years old
    old_judges = 40 - young_judges - middle_judges  # The rest of the judges are over 50 years old

    # Return the number of judges over 50 years old
    result = old_judges
    return result

print(solution())