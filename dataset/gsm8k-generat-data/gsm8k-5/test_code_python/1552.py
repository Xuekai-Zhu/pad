def solution():
    total_employees = 180  # Lauryn employs 180 people
    men_to_women_ratio = 1 / 2  # There are 20 fewer men than women, so the ratio is 1:2
    men_count = total_employees * men_to_women_ratio / (1 + men_to_women_ratio)  # Calculate the number of men
    result = men_count
    return result

print(solution())