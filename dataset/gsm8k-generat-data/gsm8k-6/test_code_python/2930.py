def solution():
    # Calculate the total earnings of the park
    group1_earnings = (12+6) * 10  # 10 people take the tour and admission
    group2_earnings = 12 * 5  # 5 people only take admission
    total_earnings = group1_earnings + group2_earnings
    result = total_earnings
    return result

print(solution())